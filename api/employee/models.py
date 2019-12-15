from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from api import db


def set_password(password):
    return generate_password_hash(password)


class Employee(UserMixin, db.Model):

    # UserMixin includes a few methods in he class that are needed by flask_login

    __tablename__ = 'employee_table'

    id = db.Column(db.String, primary_key=True)
    employee_id = db.Column(db.Integer, db.Sequence('emp_table_seq'), unique=True, index=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    password = db.Column(db.String)
    contact = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    pincode = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)
    is_manager = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get('uuid')
        # self.employee_id = generate_emp_id()
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.contact = kwargs.get('contact')
        self.email = kwargs.get('email')
        self.password = set_password(self.contact)

    @property
    def serialize(self):
        return {
            "emp_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact": self.contact,
            "email": self.email
        }

    @property
    def is_authenticated(self):
        return True

    def verify_password(self, user_password):
        return check_password_hash(self.password, user_password)
