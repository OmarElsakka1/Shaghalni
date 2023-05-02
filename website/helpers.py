from datetime import datetime
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
import re   

from .models import db, Job , User


def populate_database():
    # create business owner users
    try :
        user1 = User(email='owner1@example1.com', password='password', first_name='John', last_name='Doe', gender='male', usertype='Business Owner', job_des='Business Owner')
        user2 = User(email='owner2@example2.com', password='password', first_name='Jane', last_name='Smith', gender='female', usertype='Business Owner', job_des='Business Owner')
        db.session.add_all([user1])
        db.session.commit()

        # create job seeker users
        user3 = User(email='seeker1@example.com', password='password', first_name='Alice', last_name='Johnson', gender='female', usertype='Freelancer', job_des='Software Developer')
        user4 = User(email='seeker2@example.com', password='password', first_name='Bob', last_name='Williams', gender='male', usertype='Freelancer', job_des='Data Analyst')
        db.session.add_all([user3, user4])
        db.session.commit()
        owner1_jobs = [
        Job(job_name='Software Developer', job_payment=5000, job_description='Develop software', job_deadline=datetime.utcnow() + timedelta(days=7), user=user1),
        Job(job_name='Marketing Manager', job_payment=7000, job_description='Manage marketing campaigns', job_deadline=datetime.utcnow() + timedelta(days=14), user=user1),
        ]
        owner2_jobs = [
            Job(job_name='Data Analyst', job_payment=6000, job_description='Analyze data', job_deadline=datetime.utcnow() + timedelta(days=21), user=user2),
            Job(job_name='Customer Support Specialist', job_payement=4000, job_description='Provide customer support', job_deadline=datetime.utcnow() + timedelta(days=30), user=user2),
        ]
        db.session.add_all(owner1_jobs + owner2_jobs)
        db.session.commit()
    except :
        db.session.rollback()
        print('Database already populated.')

    

    print('Database populated successfully.')

  
  
def check_email(email):   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,email)):   
        return True   
    else:   
        return False 


    