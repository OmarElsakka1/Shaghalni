from .models import *
import os
from werkzeug.utils import secure_filename


class FileManager:
    def __init__(self) -> None:
        pass

    @staticmethod
    def IsImage(file):
        filename = secure_filename(file.filename)
        extension = filename.split('.')[-1]
        if extension in ['png','jpg','jpeg']:
            return True
        return False

    @staticmethod
    def SaveFile(file ,owner) -> str:
        filename = secure_filename(file.filename)
        extension = filename.split('.')[-1]
        if not owner: return None
        if isinstance(owner,Job):
            print("owner",owner.id)
            save_loc = os.path.join('instance','Images','Jobs',f'{owner.id}.{extension}')
            os.makedirs(os.path.dirname(save_loc), exist_ok=True)
            print(save_loc)
            file.save(save_loc)
            return save_loc
        elif isinstance(owner,User) :
            save_loc = os.path.join('instance','Images','Users',f'{owner.id}.{extension}')
            os.makedirs(os.path.dirname(save_loc), exist_ok=True)
            file.save(save_loc)
            return save_loc

        elif isinstance(owner , JobApplication) :
            save_loc = os.path.join('instance','Images','ApplicationSubmissions',f'{owner.id}.{extension}')
            os.makedirs(os.path.dirname(save_loc), exist_ok=True)
            file.save(save_loc)
            return save_loc
            
        return None
