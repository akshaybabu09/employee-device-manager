from flask import request
from flask_login import login_required, current_user
from flask_restful import Resource

from api.status_codes import *
from api.status_messages import *


class EmployeeLoginAPI(Resource):

    def post(self):
        from flask_login import login_user
        from api.employee.services import fetch_emp_from_emp_id

        try:
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


class EnrollEmployeeAPI(Resource):
    method_decorators = [login_required]

    def post(self):
        from api.employee.services import enroll_employee
        from api.employee.services import verify_if_phone_exists
        from api.employee.services import verify_if_email_exists

        try:
            phone_exists = verify_if_phone_exists(request.json.get('contact'))
            if phone_exists:
                return PHONE_EXISTS, CONFLICT
            email_exists = verify_if_email_exists(request.json.get('email'))
            if email_exists:
                return EMAIL_EXISTS, CONFLICT
            if current_user.is_manager:
                emp = enroll_employee(request.json)
                emp_data = emp.serialize

                return {"msg": EMP_ENROLLED, "data": emp_data}, OK
            return NO_ACCESS, NOT_ACCEPTABLE
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class UpdateEmployeeAPI(Resource):
    method_decorators = [login_required]

    def post(self):             # Check if PUT can be used
        from api.employee.services import update_employee_details

        try:
            if not bool(request.json):
                return DATA_EMPTY, NOT_ACCEPTABLE
            emp = current_user
            update_employee_details(emp, request.json)
            return UPDATE_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR

    def get(self):
        try:
            return OK_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class EmployeeDetailsAPI(Resource):
    method_decorators = [login_required]

    def get(self):
        from api.employee.services import fetch_employee_details

        try:
            if current_user.is_manager:
                emp_details = fetch_employee_details()
                return {"emp_details": emp_details}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class RemoveEmployeeAPI(Resource):
    method_decorators = [login_required]

    def post(self):
        from api.employee.services import remove_employee

        try:
            if current_user.is_manager:
                remove_employee(request.form['emp_id'])
                return EMPLOYEE_DELETED, OK
            return NO_ACCESS, NOT_ACCEPTABLE
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class EmployeeLogoutAPI(Resource):
    method_decorators = [login_required]

    def get(self):
        from flask_login import logout_user

        try:
            logout_user()
            return LOGOUT_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
