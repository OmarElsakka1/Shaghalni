from datetime import datetime
from .models import db, Job

def create_dummy_jobs():
    job1 = Job(
        job_name='Software Engineer',
        job_description='We are looking for a skilled software engineer to join our team.',
        job_date=datetime(2023, 5, 1),
        user_id=1
    )
    job2 = Job(
        job_name='Data Analyst',
        job_description='We are seeking a data analyst to help us analyze and interpret complex data sets.',
        job_date=datetime(2023, 5, 5),
        user_id=1
    )
    job3 = Job(
        job_name='Marketing Manager',
        job_description='We are looking for a marketing manager to develop and execute marketing campaigns.',
        job_date=datetime(2023, 5, 10),
        user_id=1
    )
    job4 = Job(
        job_name='Graphic Designer',
        job_description='We are seeking a talented graphic designer to create visually appealing designs for our company.',
        job_date=datetime(2023, 5, 15),
        user_id=1
    )
    db.session.add_all([job1, job2, job3, job4])
    db.session.commit()