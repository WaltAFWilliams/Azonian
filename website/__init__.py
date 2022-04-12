from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path


db = SQLAlchemy()
DB_NAME = path.abspath('autoz_database.db')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SuperSecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth


    from .db_create import create_database
    from .db_populate import populate_database
    
    create_database()
    populate_database()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, AtoForm

    
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    return app


def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
