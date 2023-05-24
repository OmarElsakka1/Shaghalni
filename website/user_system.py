from .models import *
from .file_manager import FileManager
from . import db
from .singelton_meta import SingletonMeta

class UserSystem(metaclass=SingletonMeta) :
    lisiteners = []
    def __init__(self,db) -> None:
        self.db = db

    def GetUser(self, id) -> User:
        '''
        Returns the user with the given id.
        '''
        return User.query.get(id)

    def SearchUsersByName(self, name : str) -> list[User]  :
        '''
        Searches for users with the given name.
        Returns a list of users.
        '''
        splitted = name.split()
        if len(splitted) == 1 :
            return User.query.filter_by(first_name = name).all()
        else :
            return User.query.filter_by(first_name = splitted[0], last_name = splitted[-1]).all()

    def ChangePfp(self,user : User , img = None) -> bool :
        if img != None :
            fname = FileManager.SaveFile(img , user)
            if fname == None :
                print("Error in saving image")
                return False
            user.image_name = fname
            db.session.commit()
            return True
        return False

    def DeleteUser(self, user_id : int) -> bool :
        '''
        Deletes the user with the given id.
        '''
        user = User.query.get(user_id)
        if user == None :
            return False
        self.db.session.delete(user)
        self.db.session.commit()
        for listener in self.listeners :
            listener.OnUserDeleted(user_id)
        return True 



userSystem = UserSystem(db)
            


    
    