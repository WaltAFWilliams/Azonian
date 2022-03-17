from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{passwd}@localhost:5432/{db_name}'
    db.init_app(app)

    from .views import views
    from .models import create_users, create_ato_forums

    create_users()
    create_ato_forums()

    app.register_blueprint(views, url_prefix='/')

    return app