from flask import request
from flask_restful import Resource

from api.utils.status_codes import INTERNAL_SERVER_ERROR, OK, BAD_REQUEST
from api.utils.status_messages import INVALID_USER, INVALID_PASS, LOGIN_MSG, ERROR_MSG


class EmployeeLoginAPI(Resource):

    def post(self):
        from api.utils.libs import generate_token
        from api.employee.service import fetch_emp_from_emp_id

        try:
            username = request.json.get('emp_id')
            password = request.json.get('password')
            emp = fetch_emp_from_emp_id(int(username))
            if not emp:
                return INVALID_USER, BAD_REQUEST
            if not emp.verify_password(password):
                return INVALID_PASS, BAD_REQUEST
            token = generate_token(emp)
            return {"token": token.decode('UTF-8'), "msg": LOGIN_MSG}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
