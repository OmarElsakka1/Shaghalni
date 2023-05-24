from .models import *
from .file_manager import FileManager
from .application_system import applicationsSystem
from . import db
from .singelton_meta import SingletonMeta


class SubmissionSystem(metaclass=SingletonMeta):
    def __init__(self,db) :
        self.db = db

    def GetSubmissionById(self, sub_id : int) -> ApplicationSubmission:
        '''
        Returns a submission by id
        '''
        return ApplicationSubmission.query.filter_by(id=sub_id).first() 

    def GetSubmissionsToUser(self,user_id) -> list:
        '''
        Returns a list of all the submissions for a user
        '''
        submissions = ApplicationSubmission.query.join(JobApplication, JobApplication.id == ApplicationSubmission.application_id) \
        .join(Job, Job.id == JobApplication.job_id).filter(Job.user_id == user_id).all()

        return submissions

    def MakeSubmission(self,application_id , title , file) -> bool:
        print(f"Making a submission for application {application_id} with title {title} ")
        app = JobApplication.query.filter_by(id=application_id).first()
        if app and app.job_status == 'Accepted' :
            print("Saving file")
            path = FileManager.SaveFile(file , owner=app)
            print(path)
            if not path :
                return False
            db.session.commit()
            submission = ApplicationSubmission(title=title,file_path=path,application_id=application_id)
            db.session.add(submission)
            db.session.commit()
            return True
        return False

    def AcceptSubmission(self,submission_id : int , user_id : int) -> bool:
        submission:ApplicationSubmission = ApplicationSubmission.query.filter_by(id=submission_id).first()
        if submission and submission.application.job.user_id == user_id :
            applicationsSystem.DeleteApplication(submission.application.id)
            return True
        return False

    def OnAppDeleted(self , app_id : int ) :
        '''
        Called when an application is deleted
        '''
        for submission in ApplicationSubmission.query.filter_by(application_id=app_id).all() :
            db.session.delete(submission)
        db.session.commit()




submissionSystem = SubmissionSystem(db)
applicationsSystem.listeners.append(submissionSystem)