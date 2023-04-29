from datetime import datetime
from flask import Blueprint, render_template, request, flash, jsonify , redirect , url_for
from flask_login import login_required, current_user
from .models import *
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # redirect tp jobs
    return redirect(url_for('views.browse_jobs'))

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/browse-jobs' , methods = ['GET' , 'POST'] )
@login_required
def browse_jobs():
    # get all jops from db
    jobs = Job.query.all()
    return render_template("browse_jobs.html" ,user=current_user ,jobs = jobs )


@views.route('/apply-job' , methods = ['GET' , 'POST'] )
@login_required
def apply_job():
    # get all jops from db
    jobs = Job.query.all()
    return "not yet"


@views.route('/post-job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        job_name = request.form['job_name']
        job_description = request.form['job_description']
        job_date_str = request.form['job_date']
        job_date = datetime.strptime(job_date_str ,'%Y-%m-%dT%H:%M')
        job = Job(job_name=job_name, job_description=job_description, job_date=job_date , user_id = current_user.id)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('views.browse_jobs'))
    else:
        return render_template('post_job.html' , user =  current_user)



@views.route('/changeprofile', methods=['GET', 'POST'])
@login_required
def change_profile():
    dropdown_options = ['Freelancer', 'Business Owner', 'Both']
     
    return render_template('change_profile.html',user=current_user, dropdown_options = dropdown_options)


