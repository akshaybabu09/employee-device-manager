from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import NOT_ACCEPTABLE, BAD_REQUEST, NOT_FOUND, OK, INTERNAL_SERVER_ERROR
from api.utils.status_messages import DATA_EMPTY, DEVICE_EXISTS, EMPLOYEE_NOT_FOUND, DEVICE_ENROLLED, ERROR_MSG


class EnrollDeviceAPI(Resource):
    method_decorators = [token_required]

    def post(self, current_user):
        from api.device.service import enroll_device, check_for_device_id, send_device_details_to_emp
        from api.employee.models import fetch_employee_from_emp_id

        try:
            if not request.json:
                return DATA_EMPTY, NOT_ACCEPTABLE
            if check_for_device_id(request.json.get('device_id')):
                return DEVICE_EXISTS, BAD_REQUEST
            emp = fetch_employee_from_emp_id(int(request.json.get('emp_id')))
            if not emp:
                return EMPLOYEE_NOT_FOUND, NOT_FOUND
            device = enroll_device(emp, request.json)
            send_device_details_to_emp.apply_async(args=[
                emp.serialize, device.serialize
            ])
            return DEVICE_ENROLLED, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
