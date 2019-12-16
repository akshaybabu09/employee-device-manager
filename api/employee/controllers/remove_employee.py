from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import INTERNAL_SERVER_ERROR, OK
from api.utils.status_messages import EMPLOYEE_DELETED, ERROR_MSG


class RemoveEmployeeAPI(Resource):
    method_decorators = [token_required]

    def post(self, current_user):
        from api.employee.service import remove_employee

        try:
            remove_employee(request.json.get('emp_id'))
            return EMPLOYEE_DELETED, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
