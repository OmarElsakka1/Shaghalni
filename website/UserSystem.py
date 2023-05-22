from .models import *
from .ImageManager import ImageManager
from . import db


class UserSystem :

    @staticmethod
    def GetUser( id) :
        return User.query.get_or_404(id)
    
    def SearchUsersByName( name : str) :
        '''
        Searches for users with the given name.
        Returns a list of users.
        '''
        splitted = name.split()
        if len(splitted) == 1 :
            return User.query.filter_by(first_name = name).all()
        else :
            return User.query.filter_by(first_name = splitted[0], last_name = splitted[-1]).all()
    