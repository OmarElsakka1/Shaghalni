from .models import *
from .FileManager import FileManager
from .ApplicationsSystem import applicationsSystem
from . import db
from .SingletonMeta import SingletonMeta


class SubmissionSystem(metaclass=SingletonMeta):
    def __init__(self,db) :
        self.db = db

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



     


submissionSystem = SubmissionSystem(db)