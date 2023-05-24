from distutils.log import error
from .models import *
from . import db
from .singelton_meta import SingletonMeta
from .job_system import jobSystem

class ApplicationsSystem(metaclass=SingletonMeta):
    listeners = []
    def __init__(self , db) -> None:
        self.db = db

    def GetApplicationById(self , application_id : int) -> JobApplication :
        ''' 
            Returns the application with the given id
            If no application with the given id exists, returns None.
        
        '''
        return JobApplication.query.filter_by(id = application_id).first()

    def GetPendingApplications(self, job_id : int) -> list[JobApplication] :
        '''
            Returns a list of all pending applications for the given job
        '''
        
        return JobApplication.query.filter_by(job_id = job_id , status = "Pending").all()        

    def PostApplication(self, job_id : int , applicant_id : int) -> JobApplication :
        job_application = JobApplication(job_id = job_id , user_id = applicant_id , job_status = 'Pending')
        self.db.session.add(job_application)
        self.db.session.commit()

    def AcceptApplication(self, job_application_id : int) -> bool :
        ''' 
            Accepts the application with the given id.
            Returns True if the application was accepted, False otherwise.
        '''
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

    def DeleteApplication(self , application_id : int) -> bool :
        try :
            application = JobApplication.query.filter_by(id = application_id).first()
            application.delete()
            self.db.session.commit()
            return True
        except :
            return False
            
    def GetApplicationsByUser(self , user_id : int) -> list[JobApplication] :
        return JobApplication.query.filter_by(user_id = user_id).all()

    def OnJobDeleted(self , job_id : int) -> None :
        try : 
            deleted_app =  JobApplication.query.filter_by(job_id = job_id).first()
            if deleted_app :
                for listener in self.listeners :
                    listener.OnAppDeleted(job_id)
            deleted_app.delete()
            self.db.session.commit()
        except :
            print("No applications to delete")
    


applicationsSystem = ApplicationsSystem(db)
jobSystem.listeners.append(applicationsSystem) 