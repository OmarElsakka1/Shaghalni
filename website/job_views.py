from datetime import datetime
from flask import Blueprint, render_template, request, flash , redirect , url_for
from flask_login import login_required, current_user
from .JobSystem import jobSystem
from .models import Job
from . import db


job_views = Blueprint('job_views', __name__)

@job_views.route('/browse-jobs' , methods = ['GET' , 'POST'] )
@login_required
def browse_jobs():
    jobs = jobSystem.GetAllJobs()
    return render_template("browse_jobs.html" ,user=current_user ,jobs = jobs )


@job_views.route('/jobs/<int:job_id>/apply', methods=['POST'])
@login_required
def apply_job(job_id):
    jobSystem.ApplyForJob(job_id, current_user.id)
    print(f"Applied to job with id {job_id}")
    return redirect(url_for('job_views.browse_jobs'))

@job_views.route('/post_job', methods=['GET', 'POST'])
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
        return redirect(url_for('job_views.browse_jobs'))
    return render_template('post_job.html' ,user = current_user)