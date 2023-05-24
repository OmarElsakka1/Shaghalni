import os
from os import path
from flask import Flask
from flask_login import LoginManager
from .models import db, DB_NAME
from .helpers import *
from .views import views
from .auth import auth
from .admin_views import admin
from .job_views import job_views
from .profile_views import profile_views


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
        create_images_folder(app)

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')
        app.register_blueprint(job_views, url_prefix='/')
        app.register_blueprint(profile_views, url_prefix='/')
        app.register_blueprint(admin_views, url_prefix='/admin')

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


def create_images_folder(app):
    if not path.exists('instance/Images'):
        os.mkdir('instance/Images')
        print('Images folder created.')
    if not path.exists('instance/Statistics'):
        os.mkdir('instance/Statistics')
        print('Statistics images folder created.')
