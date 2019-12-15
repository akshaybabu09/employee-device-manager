import uuid

from api import db, login_manager

from .models import Employee
from ..device.models import fetch_devices_from_emp_uuid


def enroll_employee(emp_data):
    emp = Employee(
        uuid=generate_id(),
        first_name=emp_data.get('first_name'),
        last_name=emp_data.get('last_name'),
        contact=emp_data.get('contact'),
        email=emp_data.get('email')
    )
    if emp_data.get('is_manager'):
        emp.is_manager = True
    db.session.add(emp)
    db.session.commit()
    return emp


def verify_if_phone_exists(contact):
    emp = Employee.query.filter(Employee.contact == contact).first()
    if emp:
        return True
    return False


def verify_if_email_exists(email):
    emp = Employee.query.filter(Employee.email == email).first()
    if emp:
        return True
    return False


def generate_id():
    return str(uuid.uuid4())


def fetch_emp_from_emp_id(emp_id):
    return Employee.query.filter(Employee.employee_id == emp_id).first()


def update_employee_details(emp, request_json):
    emp.contact = request_json.get('contact', emp.contact)
    emp.email = request_json.get('email', emp.email)
    emp.address = request_json.get('address', emp.address)
    emp.pincode = request_json.get('pincode', emp.pincode)
    db.session.add(emp)
    db.session.commit()


def remove_employee(emp_id):
    emp = Employee.query.filter(Employee.employee_id == emp_id).first()
    emp.is_active = False
    db.session.add(emp)
    db.session.commit()


def fetch_employee_details():
    query_set = Employee.query.filter(
        Employee.is_manager == False,
        Employee.is_active == True
    ).all()

    emp_details = {}

    for emp in query_set:
        emp_detail = emp.serialize
        emp_detail['device_details'] = fetch_devices_from_emp_uuid(emp.id)
        emp_details[emp.employee_id] = emp_detail
    return emp_details


@login_manager.user_loader
def load_user(user_id):
    """
        Loads a user for flask login.
        :param user_id: ID of the user.
        :return: The user object
    """
    return Employee.query.filter(Employee.id == user_id).first()
