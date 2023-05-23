from .models import *
from .ImageManager import ImageManager
from .ApplicationsSystem import applicationsSystem
from . import db
from .SingletonMeta import SingletonMeta


class SubmissionSystem(metaclass=SingletonMeta):
    def __init__(self,db) :
        self.db = db


submissionSystem = SubmissionSystem(db)