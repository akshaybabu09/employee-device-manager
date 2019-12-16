import os

from celery import Celery
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['SECRET_KEY'] = "\x1c{fE\xf8\x7f[l\xfd\xdd9\xef\tX\xccc\x14\xd27q\xbf@\xe1\xcb"
    db = SQLAlchemy(app=app)
    db.init_app(app)

    return app, db


app, db = create_app()

app.config['SESSION_SQLALCHEMY'] = db
Session(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

celery = Celery(
    'api',
    broker=app.config['CELERY_BROKER_URL'],
    include=[
        'api.device.service'
    ]
)

app.config.update(
    DEBUG=True,
    # Email Settings
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ['HOST_EMAIL'],
    MAIL_PASSWORD=os.environ['HOST_PASSWORD']
)
mail = Mail(app)

# Models
from api.employee.models import Employee
from api.device.models import Device


db.create_all()


@app.route('/')
def hello():
    return 'Hello, World!'
