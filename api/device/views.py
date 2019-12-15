from flask import request
from flask_login import login_required, current_user
from flask_restful import Resource

from api.device.service import enroll_device, check_for_device_id, update_device_details, fetch_device_details, \
    remove_device
from api.employee.models import fetch_employee_from_emp_id
from api.status_codes import *
from api.status_messages import *


class EnrollDeviceAPI(Resource):
    method_decorators = [login_required]

    def post(self):
        try:
            if not request.json:
                return DATA_EMPTY, NOT_ACCEPTABLE
            if current_user.is_manager:
                if check_for_device_id(request.json.get('device_id')):
                    return DEVICE_EXISTS, BAD_REQUEST
                emp = fetch_employee_from_emp_id(int(request.json.get('emp_id')))
                if not emp:
                    return EMPLOYEE_NOT_FOUND, NOT_FOUND
                enroll_device(emp, request.json)
                return DEVICE_ENROLLED, OK
            return NO_ACCESS, NOT_ACCEPTABLE
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class UpdateDeviceDetailsAPI(Resource):
    method_decorators = [login_required]

    def post(self):
        try:
            if not request.json:
                return DATA_EMPTY, NOT_ACCEPTABLE
            update_device_details(request.json)
            return UPDATE_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class DisplayDeviceDetailsAPI(Resource):
    method_decorators = [login_required]

    def get(self):
        try:
            if current_user.is_manager:
                device_details = fetch_device_details()
                return {'device_details': device_details}, OK
            return NO_ACCESS, NOT_ACCEPTABLE
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR


class RemoveDeviceAPI(Resource):
    method_decorators = [login_required]

    def post(self):
        try:
            if current_user.is_manager:
                remove_device(request.form['device_id'])
                return DEVICE_REMOVED, OK
            return NO_ACCESS, NOT_ACCEPTABLE
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR

