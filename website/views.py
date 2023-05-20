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
    for job in jobs :
        print(type(job.job_payment) )
    return render_template("browse_jobs.html" ,user=current_user ,jobs = jobs )


@views.route('/jobs/<int:job_id>/apply', methods=['POST'])
@login_required
def apply_job(job_id):
    job = Job.query.get_or_404(job_id)
    print(f"Applied to job with id {job_id}")
    return redirect(url_for('views.browse_jobs'))



@views.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    
    if request.method == 'POST':
        job_name = request.form['job_name']
        job_description = request.form['job_description']
        job_payment = request.form['job_payment']

        job_deadline = request.form['job_deadline']
        job_deadline = datetime.strptime(job_deadline, '%Y-%m-%d' )
        job = Job(job_name=job_name, job_description=job_description, job_payment=job_payment,  job_deadline=job_deadline, user=current_user)
        db.session.add(job)
        db.session.commit()
        flash('Your job has been posted!', 'success')
        return redirect(url_for('views.browse_jobs'))
    return render_template('post_job.html' ,user = current_user)


