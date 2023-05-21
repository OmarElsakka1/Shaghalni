from .models import *
from . import db



class JobSystem :
    def __init__(self , db) -> None:
        self.db = db

    def PostJob(self , job :Job , img : None ):
        self.db.session.add(job)
        self.db.session.commit()
        return True
    
    def GetAllJobs(self):
        print("Getting all jobs")
        return Job.query.all()
        
    def GetJob(self , id):
        return Job.query.get_or_404(id)

    def ApplyForJob(self , job_id , user_id) :
        print("Applying for a job")
        try :
            job = Job.query.get(job_id)
            user = User.query.get(user_id)
            if not job or not user :
                print("User or job not found")
                return False
            job_application = JobApplication(job_id = job_id , user_id = user_id)
            self.db.session.add(job_application)
            self.db.session.commit()
            return True
        except:
            print("Error in applying for job")
            return False
            
        

    def DeleteJob(self , id):
        try:
            job = Job.query.get(id)
            self.db.session.delete(job)
            self.db.session.commit()
            return True
        except:
            return False
        

jobSystem = JobSystem(db)