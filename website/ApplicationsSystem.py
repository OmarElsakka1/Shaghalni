from .models import *
from . import db
from .SingletonMeta import SingletonMeta

class ApplicationsSystem(SingletonMeta):
    def __init__(self , db) -> None:
        self.db = db

    def GetPendingApplications(self, job_id : int) -> list[JobApplication] :
        return JobApplication.query.filter_by(job_id = job_id , status = "Pending").all()        

    def PostApplication(self, job_id : int , applicant_id : int) -> JobApplication :
        job_application = JobApplication(job_id = job_id , user_id = applicant_id , job_status = 'Pending')
        self.db.session.add(job_application)
        self.db.session.commit()

    def AcceptApplication(self, job_application_id : int) -> None :
        try :
            job_application = JobApplication.query.filter_by(id = job_application_id).first()
            job_application.status = "Accepted"
            self.db.session.commit()
            return True
        except:
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
