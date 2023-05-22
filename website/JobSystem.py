from .models import *
from .ImageManager import ImageManager
from . import db



class JobSystem :
    def __init__(self , db) -> None:
        self.db = db

    def PostJob(self , job :Job , img : None ):
        self.db.session.add(job)
        self.db.session.commit()
        if img != None :
            fname = ImageManager.SaveImage(img , job)
            if fname == None :
                print("Error in saving image")
                self.db.session.delete(job)
                self.db.session.commit()
                return False
            
            job_image = JobImage(job_id = job.id , image_path = fname)
            self.db.session.add(job_image)
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
            
        
    def GetJobImage(self , job_id : int) -> JobImage:
        """ 
        Args:
            job_id (int): _description_

        Returns:
            JobImage: 
        """        
        return JobImage.query.filter_by(job_id = job_id).first()

    def DeleteJob(self , id : int):
        """ 
        Delete a job from the database.
        Args:
            id (int): id of the job
        
        Returns:
            bool: True if job deleted else False.
        """        
       
        try:
            job = Job.query.get(id)
            self.db.session.delete(job)
            self.db.session.commit()
            return True
        except:
            return False
        

jobSystem = JobSystem(db)