from distutils import extension
from fileinput import filename
from .models import *
import os
from werkzeug.utils import secure_filename
from PIL import Image




class ImageManager:
    def __init__(self) -> None:
        pass

    @staticmethod
    def CheckExtension(file):
        filename = secure_filename(file.filename)
        extension = filename.split('.')[-1]
        if extension in ['png','jpg','jpeg']:
            return True
        return False

    @staticmethod
    def SaveImage(file ,owner):
        filename = secure_filename(file.filename)
        extension = filename.split('.')[-1]
 
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
            file.save(f'instance/Images/Users/{owner.id}.{extension}')
            return save_loc
            
        return None
