from flask import request
from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import INTERNAL_SERVER_ERROR, NOT_ACCEPTABLE, OK
from api.utils.status_messages import EMPLOYEE_DELETED, NO_ACCESS, ERROR_MSG


class RemoveEmployeeAPI(Resource):
    method_decorators = [token_required]

    def post(self, current_user):
        from api.employee.services import remove_employee

        try:
            remove_employee(request.form['emp_id'])
            return EMPLOYEE_DELETED, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
