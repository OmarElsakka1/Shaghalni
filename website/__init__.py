from flask import Flask
from os import path
from .models import db , DB_NAME
from flask_login import LoginManager
from .helpers import *



def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        db.init_app(app)

        from .views import views
        from .auth import auth

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')

        from .models import User, Note
        
        with app.app_context():
            db.create_all()

        populate_database()
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
