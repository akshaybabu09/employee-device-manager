from flask import Blueprint
from flask_restful import Api

from api.employee.views import EnrollEmployeeAPI
from api.employee.views import EmployeeLoginAPI
from api.employee.views import EmployeeLogoutAPI

employee_blueprint = Blueprint('employee_blueprint_v1', __name__)
api = Api(employee_blueprint, prefix='/api/v1/employee')

api.add_resource(EnrollEmployeeAPI, '/enroll', strict_slashes=False)
api.add_resource(EmployeeLoginAPI, '/login', strict_slashes=False)
api.add_resource(EmployeeLogoutAPI, '/logout', strict_slashes=False)
