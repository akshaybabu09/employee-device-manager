import random

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from api import db


class Employee(UserMixin, db.Model):

    # UserMixin includes a few methods in he class that are needed by flask_login

    __tablename__ = 'employee_table'

    id = db.Column(db.String, primary_key=True)
    employee_id = db.Column(db.Integer, unique=True, index=True)
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
        self.employee_id = generate_emp_id()
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


def set_password(password):
    return generate_password_hash(password)


def fetch_employee_from_uuid(emp_uuid):
    emp = Employee.query.filter(Employee.id == emp_uuid).first()
    return emp.serialize


def fetch_employee_from_emp_id(emp_id):
    return Employee.query.filter(
        Employee.employee_id == emp_id,
        Employee.is_active == True,
        Employee.is_manager == False
    ).first()


def fetch_random_employee():
    query_set = db.session.query(Employee.id).filter(
        Employee.is_active == True, Employee.is_manager == False
    ).all()
    emp_ids = [item for query in query_set for item in query]
    emp_id = random.choice(emp_ids)
    return emp_id


def generate_emp_id():
    emp_id = random.randint(100000, 999999)
    emp = Employee.query.filter(Employee.employee_id == emp_id).first()
    if emp:
        return generate_emp_id()
    return emp_id
