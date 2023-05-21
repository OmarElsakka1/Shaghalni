from flask import Flask
from os import path
from .models import db , DB_NAME
from flask_login import LoginManager
from .helpers import *
from .views import views
from .auth import auth
from .admin import admin
from .job_views import job_views
import os


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        # added by Sakka
        app.config['UPLOAD_FOLDER'] = 'instance/Images/'
        app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
        #
        db.init_app(app)
        create_Images_Folder(app)

        

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')
        app.register_blueprint(job_views , url_prefix = '/' )
        app.register_blueprint(admin, url_prefix='/admin')

        from .models import User
        
        with app.app_context():
            db.create_all()

        populate_database()
        Adding_Initial_Admin()
        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))

        return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

def create_Images_Folder(app):
    if not path.exists('instance/Images'):
        os.mkdir('instance/Images')
        print('Images folder created.')
    if not path.exists('instance/Statistics'):
        os.mkdir('instance/Statistics')
        print('Statistics images folder created.')
