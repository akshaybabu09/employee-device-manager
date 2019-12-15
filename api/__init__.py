import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'thisissecretkey'
    db = SQLAlchemy(app=app)
    db.init_app(app)

    return app, db


app, db = create_app()

app.config['SESSION_SQLALCHEMY'] = db
Session(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
# celery = make_celery(app)


# Models
from api.employee.models import Employee


db.create_all()


@app.route('/')
def hello():
    return 'Hello, World!'
