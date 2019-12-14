import uuid

from api import db, login_manager

from .models import Employee


def enroll_employee(emp_data):
    emp = Employee(
        uuid=generate_id(),
        first_name=emp_data.get('first_name'),
        last_name=emp_data.get('last_name'),
        contact=emp_data.get('contact'),
        email=emp_data.get('email')
    )
    # emp.set_password(emp_data.get('contact'))
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
    # print(type(emp))
    print(request_json)



@login_manager.user_loader
def load_user(user_id):
    """
        Loads a user for flask login.
        :param user_id: ID of the user.
        :return: The user object
    """
    return Employee.query.filter(Employee.id == user_id).first()
