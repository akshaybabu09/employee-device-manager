from flask import request, g
from flask_login import login_user, login_required, logout_user
from flask_restful import Resource

from api.employee.services import enroll_employee, verify_if_phone_exists, verify_if_email_exists, load_user, \
    fetch_emp_from_emp_id, update_employee_details
from api.status_codes import *
from api.status_messages import *


class EnrollEmployeeAPI(Resource):

    def post(self):
        try:
            phone_exists = verify_if_phone_exists(request.json.get('contact'))
            if phone_exists:
                return PHONE_EXISTS, CONFLICT
            email_exists = verify_if_email_exists(request.json.get('email'))
            if email_exists:
                return EMAIL_EXISTS, CONFLICT
            emp = enroll_employee(request.json)
            emp_data = emp.serialize

            return {"msg": EMP_ENROLLED, "data": emp_data}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class EmployeeLoginAPI(Resource):

    def post(self):
        try:
            print(request.form)
            username = request.form['emp_id']
            password = request.form['password']
            emp = fetch_emp_from_emp_id(int(username))
            if not emp:
                return INVALID_USER, BAD_REQUEST
            if not emp.verify_password(password):
                return INVALID_PASS, BAD_REQUEST
            if not login_user(emp):
                return LOGIN_FAIL, BAD_REQUEST
            return LOGIN_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class EmployeeLogoutAPI(Resource):
    method_decorators = [login_required]

    def get(self):
        try:
            value = logout_user()
            print(value)
            return LOGOUT_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
