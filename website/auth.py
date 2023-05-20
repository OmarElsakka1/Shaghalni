from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from .helpers import CheckTypicality, CheckLength, Passwords, Check_email
from flask_wtf.file import FileField, FileRequired
import os

from flask import send_file
from io import BytesIO


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if Passwords(user.password,password).Is_same('Logged in successfully!', 'Incorrect password, try again.'):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    dropdown_options = ['Freelancer', 'Business Owner', 'Both']
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        gender = request.form['gender']
        usertype = request.form['usertype']
        job_des = request.form.get('job_description')
        

        user = User.query.filter_by(email=email).first()
        IsGoodpass = Passwords(password1, password2).is_good()
        IsGoodemail = Check_email().is_in_form(email)

        firstcheck = CheckLength(2,"First name").is_short(first_name)
        lastcheck = CheckLength(2,"Last name").is_short(last_name)
        jobcheck = CheckLength(4, "Job Description").is_short(job_des)
        if user:
            flash('Email already exists.', category='error')
        elif firstcheck or lastcheck or jobcheck or not(IsGoodemail and IsGoodpass):  # Demorgan
            pass
        elif CheckTypicality(gender, "").is_equal():  
            flash('You have to choose a Gender.', category='error')
        elif CheckTypicality(usertype, "").is_equal(): 
            flash('You have to choose a User Type.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name = last_name,job_des = job_des, 
                 gender = gender, usertype = usertype, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user, dropdown_options = dropdown_options)



@auth.route('/changeprofile', methods=['GET', 'POST'])
@login_required
def change_profile():
    dropdown_options = ['Freelancer', 'Business Owner', 'Both']
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        gender = request.form['gender']
        usertype = request.form['usertype']
        job_des = request.form.get('job_description')
        file = request.files['file']

        user = User.query.filter_by(id=current_user.id).first()
        IsGoodemail = Check_email().is_in_form(email)

        if len(email) == 0 or not IsGoodemail:
            pass
        elif not (CheckTypicality(email, current_user.email).is_equal() or User.query.filter_by(email=email).first()):
            user.email = email
            db.session.commit()
            flash('Email changed Successfully.', category='success')
        

        if len(first_name) == 0:
            pass
        elif not (CheckLength(2,"First name").is_short(first_name) or CheckTypicality(first_name, current_user.first_name).is_equal()):
            user.first_name = first_name
            db.session.commit()
            flash('First name changed Successfully.', category='success')

        if len(last_name) == 0:
            pass
        elif not (CheckLength(2,"Last name").is_short(last_name) or CheckTypicality(last_name, current_user.last_name).is_equal()):
            user.last_name = last_name
            db.session.commit()
            flash('Last name changed Successfully.', category='success')
        
        if not (CheckLength(4,"Job Description").is_short(job_des) or CheckTypicality(job_des, current_user.job_des).is_equal()):
            user.job_des = job_des
            db.session.commit()
            flash('Job Description updated Successfully.', category='success')
            
        if not (CheckTypicality(gender, current_user.gender).is_equal() or CheckTypicality(gender, "").is_equal()):
            user.gender = gender
            db.session.commit()
            flash('Gender updated Successfully.', category='success')
        if not (CheckTypicality(usertype, current_user.usertype).is_equal() or CheckTypicality(usertype, "").is_equal()):
            user.usertype = usertype
            db.session.commit()
            flash('User Type updated Successfully.', category='success')

        if (file.filename):
            filename = file.filename
            img_format = filename[-3:]
            if (filename and ( (filename[-3:] in ['png', 'jpg', 'gif']) or (filename[-4:] == 'jpeg') ) ):
                current_user.file = file
                file.save('instance/Images/{}.{}'.format(current_user.id,img_format))
                flash('Image uploaded successfully', category='success')
            else:
                flash('Invalid Image format (Should be .jpg).', category='error')
        
        return redirect(url_for('auth.change_profile'))
    return render_template("change_profile.html", user=current_user, dropdown_options = dropdown_options)



@auth.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        email = current_user.email
        password = request.form.get('password')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(id=current_user.id).first()  

        IsGood = Passwords(password1, password2).is_good()
        IsOldCorrect = Passwords(user.password, password).Is_same("",'Old Password is wrong.')
        if (IsGood and IsOldCorrect):
            new_password_hash = generate_password_hash(password1)
            user.password = new_password_hash
            db.session.commit()
            flash('Password Changed!', category='success')
            return redirect(url_for('auth.change_password'))

    return render_template("change_password.html", user=current_user)



@auth.route('/image/<int:user_id>')
@login_required
def get_image(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        try:
            # return send_file(BytesIO(user.image_data), mimetype='image/jpeg')
            return send_file(f'../instance/Images/{user_id}.jpg', mimetype='image/jpg')
        except:
            try:
                return send_file(f'../instance/Images/{user_id}.png', mimetype='image/jpg')
            except:
                try:
                    return send_file(f'../instance/Images/{user_id}.gif', mimetype='image/jpg')
                except:
                    try:
                        return send_file(f'../instance/Images/{user_id}.jpeg', mimetype='image/jpg')
                    except:
                        return send_file('static/Images/default_profile_image.png', mimetype='image/jpg')
