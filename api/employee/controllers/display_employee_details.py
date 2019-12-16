from flask_restful import Resource

from api.utils.decorators import token_required
from api.utils.status_codes import INTERNAL_SERVER_ERROR, OK
from api.utils.status_messages import ERROR_MSG


class EmployeeDetailsAPI(Resource):
    method_decorators = [token_required]

    def get(self, current_user):

        try:
            emp_details = current_user.serialize
            return {"emp_details": emp_details}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
