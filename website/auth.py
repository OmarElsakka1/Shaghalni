from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
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
        job_des = request.form.get('job_description')
        category = request.form.get('category')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif len(job_des) < 4:
            flash('Job Description should be greater than 3 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name = last_name,
                 job_des = job_des, category = category, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            #new_user.email = "new_email@example.com"
            #db.session.add(new_user)
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
        job_des = request.form.get('job_description')
        #category = request.form.get('category')

        user = User.query.filter_by(id=current_user.id).first()
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif (email != current_user.email) and not (User.query.filter_by(email=email).first()):
            user.email = email
            db.session.commit()
            flash('Email changed Successfully.', category='success')
        else:
            pass
            #flash('Email already has account. Choose another email.', category='error')
        if len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif first_name != current_user.first_name:
            user.first_name = first_name
            db.session.commit()
            flash('First name changed Successfully.', category='success')
        if len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')

        elif last_name != current_user.last_name:
            user.last_name = last_name
            db.session.commit()
            flash('Last name changed Successfully.', category='success')
        if len(job_des) < 4:
            flash('Job Description should be greater than 3 characters.', category='error')
        elif(job_des != current_user.job_des):
            user.job_des = job_des
            db.session.commit()
            flash('Job Description updated Successfully.', category='success')
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
        if not check_password_hash(user.password, password):
            flash('Old Password is wrong.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_password_hash = generate_password_hash(password1)
            user.password = new_password_hash
            db.session.commit()
            flash('Password Changed!', category='success')
            return redirect(url_for('auth.change_password'))

    return render_template("change_password.html", user=current_user)
