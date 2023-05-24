from distutils.log import error
from .models import *
from . import db
from .SingletonMeta import SingletonMeta
from .JobSystem import jobSystem

class ApplicationsSystem(metaclass=SingletonMeta):
    def __init__(self , db) -> None:
        self.db = db

    def GetApplicationById(self , application_id : int) -> JobApplication :
        return JobApplication.query.filter_by(id = application_id).first()

    def GetPendingApplications(self, job_id : int) -> list[JobApplication] :
        return JobApplication.query.filter_by(job_id = job_id , status = "Pending").all()        

    def PostApplication(self, job_id : int , applicant_id : int) -> JobApplication :
        job_application = JobApplication(job_id = job_id , user_id = applicant_id , job_status = 'Pending')
        self.db.session.add(job_application)
        self.db.session.commit()

    def AcceptApplication(self, job_application_id : int) -> bool :
        print(f"Accepting application with id {job_application_id}...")
        try :
            job_application = JobApplication.query.filter_by(id = job_application_id).first()
            print(job_application)
            job_application.job_status = "Accepted"
            self.db.session.commit()
            print("Success")
            return True
        except error as e:
            print(e)
            return False

    def GetApplicationsByUser(self , user_id : int) -> list[JobApplication] :
        return JobApplication.query.filter_by(user_id = user_id).all()

    def OnJobDeleted(self , job_id : int) -> None :
        try : 
            JobApplication.query.filter_by(job_id = job_id).delete()
            self.db.session.commit()
        except :
            print("No applications to delete")
    


applicationsSystem = ApplicationsSystem(db)
jobSystem.listeners.append(applicationsSystem) 