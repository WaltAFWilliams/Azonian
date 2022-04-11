from flask import Flask


def create_app():
    app = Flask(__name__)
    from .db_create import create_database
    from .db_populate import populate_database

    create_database()
    populate_database()

    from .views import views
    from .models import insert_user, retrieve_users

    app.register_blueprint(views, url_prefix='/')


    return app
