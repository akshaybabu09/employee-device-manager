from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import OK, INTERNAL_SERVER_ERROR
from api.utils.status_messages import ERROR_MSG


class DisplayDeviceDetailsAPI(Resource):
    method_decorators = [token_required]

    def get(self, current_user):
        from api.device.service import fetch_device_details

        try:
            device_id = request.args.get('device_id')
            if device_id:
                device_details = fetch_device_details(device_id)
            else:
                device_details = fetch_device_details(device_id)
            return {'device_details': device_details}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
