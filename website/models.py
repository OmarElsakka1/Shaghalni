from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, Numeric

from sqlalchemy import Column, Numeric

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    usertype = db.Column(db.String(10), nullable=False)
    job_des = db.Column(db.String(400)  )
    jobs = db.relationship('Job' , backref='user')


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(150) , nullable =False)
    job_payment = db.Column(db.Numeric(10, 2), nullable=False)
    job_description = db.Column(db.String(1000) , nullable =False)
    job_date = db.Column(db.DateTime(timezone=True), default=func.now() ,nullable =False)
    job_deadline = db.Column(db.DateTime(timezone=True), nullable =False )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') , nullable =False)

