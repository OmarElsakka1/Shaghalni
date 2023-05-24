import re
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from .models import db, Job, User, Admin


def Adding_Initial_Admin():
    try:
        admin1 = Admin(
            email='admin1@Shaghlni.com',
            password=generate_password_hash(
                '1234567',
                method='sha256'),
            first_name='Omar',
            last_name='ElSakka')
        admin2 = Admin(
            email='admin2@Shaghlni.com',
            password=generate_password_hash(
                '1234567',
                method='sha256'),
            first_name='Omar',
            last_name='ElSakka')
        db.session.add_all([admin1, admin2])
        db.session.commit()
    except BaseException:
        db.session.rollback()
        print('Admin already Adding.')


def populate_database():
    # create business owner users
    try:
        user1 = User(
            email='owner1@example1.com',
            password=generate_password_hash(
                'password',
                method='sha256'),
            first_name='John',
            last_name='Doe',
            gender='Male',
            usertype='Business Owner',
            about='Business Owner')
        user2 = User(
            email='owner2@example2.com',
            password=generate_password_hash(
                'password',
                method='sha256'),
            first_name='Jane',
            last_name='Smith',
            gender='Female',
            usertype='Business Owner',
            about='Business Owner')
        db.session.add_all([user1, user2])
        db.session.commit()
    except BaseException:
        db.session.rollback()
        print("Error in creating : batch1")

    try:
        # create job seeker users
        user3 = User(
            email='seeker1@example.com',
            password=generate_password_hash(
                'password',
                method='sha256'),
            first_name='Alice',
            last_name='Johnson',
            gender='Female',
            usertype='Freelancer',
            about='Software Developer')
        user4 = User(
            email='seeker2@example.com',
            password=generate_password_hash(
                'password',
                method='sha256'),
            first_name='Bob',
            last_name='Williams',
            gender='Male',
            usertype='Freelancer',
            about='Data Analyst')
        db.session.add_all([user3, user4])
        db.session.commit()

    except IntegrityError as e:
        # print error details
        print(e)
        db.session.rollback()
        print('Database already populated.')

    try:
        # create jobs
        owner1_jobs = [Job(job_name='Software Developer',
                           job_payment=5000,
                           job_description='Develop software',
                           job_deadline=datetime.utcnow() + timedelta(days=7),
                           user=user1),
                       Job(job_name='Marketing Manager',
                           job_payment=7000,
                           job_description='Manage marketing campaigns',
                           job_deadline=datetime.utcnow() + timedelta(days=14),
                           user=user1),
                       ]
        owner2_jobs = [Job(job_name='Data Analyst',
                           job_payment=6000,
                           job_description='Analyze data',
                           job_deadline=datetime.utcnow() + timedelta(days=21),
                           user=user2),
                       Job(job_name='Customer Support Specialist',
                           job_payment=4000,
                           job_description='Provide customer support',
                           job_deadline=datetime.utcnow() + timedelta(days=30),
                           user=user2),
                       ]
        db.session.add_all(owner1_jobs + owner2_jobs)
        db.session.commit()
    except IntegrityError as e:
        # print error details
        print(e)
        db.session.rollback()
        print('Database already populated.')


class CheckTypicality:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def is_equal(self):
        if (self.word1 == self.word2):
            return True
        else:
            return False


class CheckLength:
    def __init__(self, min_len, name):
        self.min_len = min_len
        self.text = name

    def is_short(self, showmsg=False):
        if (len(self.text) < self.min_len):
            if showmsg:
                flash('{} must be at least {} characters!'.format(self.text, self.min_len), category='error')
            return True
        else:
            return False


class Passwords:
    def __init__(self, new_password, confirm_new_password):
        self.new_password = new_password
        self.confirm_new_password = confirm_new_password

    def is_good(self  ,display = True):
        if not CheckTypicality(
                self.new_password,
                self.confirm_new_password).is_equal():
            if display:
                flash('Passwords don\'t match!', category='error')
            return False
        elif CheckLength(7,self.new_password ).is_short():
            return False
        else:
            return True
        



class CheckEmail:
    def __init__(self):
        self.regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'

    def is_in_form(self, email, showmsg):
        if(re.search(self.regex, email)):
            return True
        else:
            if (showmsg):
                flash('Email has Invalid format!', category='error')
            return False
