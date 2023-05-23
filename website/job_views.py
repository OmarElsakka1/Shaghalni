from datetime import datetime
from flask import Blueprint, render_template, request, flash , redirect , url_for , session , send_file
from flask_login import login_required, current_user
from .ImageManager import  ImageManager
from .JobSystem import jobSystem
from .models import Job
import os 

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
        job_details = request.form['details']
        job_payment = request.form['job_payment']
        job_deadline = request.form['job_deadline']
        file = request.files['img']
        print(file)
        job_deadline = datetime.strptime(job_deadline, '%Y-%m-%d' )
        if file.filename :
            if not ImageManager.CheckExtension(file) :
                flash('Invalid file type', 'danger')
                return render_template('post_job.html' ,user = current_user)
        else :
            file = None
        job = Job(job_name=job_name, job_description=job_description,  job_details = job_details,job_payment=job_payment,  job_deadline=job_deadline, user=current_user)
        if  jobSystem.PostJob(job , file):
            flash('Your job has been posted!', 'success')
            return redirect(url_for('job_views.browse_jobs'))
        else : 
            flash('Something went wrong!', 'error')
            return render_template('post_job.html' ,user = current_user)
           
    return render_template('post_job.html' ,user = current_user)

@job_views.route('/jobs/<int:job_id>/expand', methods=['GET' , 'POST'])
@login_required
def expand_job(job_id):
    job = jobSystem.GetJob(job_id)
    img = get_job_image(job_id)
    return render_template('job_expanded.html', job=job, user=current_user , img = img)


@job_views.route('/jobs/<int:job_id>/get-image', methods=['GET'])
@login_required
def get_job_image(job_id):
    job_img = jobSystem.GetJobImage(job_id)
    if job_img :
        print(job_img.image_path)
        return send_file('../' + job_img.image_path, mimetype='image/jpg')
    else :
        return None