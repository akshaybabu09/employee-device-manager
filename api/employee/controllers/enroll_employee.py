from flask import request
from flask_restful import Resource

from api.utils.status_codes import INTERNAL_SERVER_ERROR, CONFLICT, OK
from api.utils.status_messages import PHONE_EXISTS, EMAIL_EXISTS, EMP_ENROLLED, ERROR_MSG


class EnrollEmployeeAPI(Resource):

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
            emp = enroll_employee(request.json)
            emp_data = emp.serialize

            return {"msg": EMP_ENROLLED, "data": emp_data}, OK
        except:
            return ERROR_MSG, INTERNAL_SERVER_ERROR
