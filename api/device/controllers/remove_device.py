from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import OK, NOT_ACCEPTABLE, INTERNAL_SERVER_ERROR
from api.utils.status_messages import DEVICE_REMOVED, NO_ACCESS, ERROR_MSG


class RemoveDeviceAPI(Resource):
    method_decorators = [token_required]

    def post(self, current_user):
        from api.device.service import remove_device, send_device_unassignment_details_to_emp
        from api.employee.models import fetch_employee_from_uuid

        try:
            device = remove_device(request.form['device_id'])
            emp = fetch_employee_from_uuid(device.assigned_employee_id)
            send_device_unassignment_details_to_emp.apply_async(
                args=[emp, device.serialize]
            )
            return DEVICE_REMOVED, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
