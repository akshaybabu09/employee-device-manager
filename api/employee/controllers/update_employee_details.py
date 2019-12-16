from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import NOT_ACCEPTABLE, OK, INTERNAL_SERVER_ERROR
from api.utils.status_messages import DATA_EMPTY, UPDATE_MSG, ERROR_MSG


class UpdateEmployeeAPI(Resource):
    method_decorators = [token_required]

    def put(self, current_user):
        from api.employee.service import update_employee_details

        try:
            if not bool(request.json):
                return DATA_EMPTY, NOT_ACCEPTABLE
            update_employee_details(current_user, request.json)
            return UPDATE_MSG, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR

