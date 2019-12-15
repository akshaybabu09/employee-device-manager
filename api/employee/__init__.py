from flask import Blueprint
from flask_restful import Api

from api.employee.views import EnrollEmployeeAPI
from api.employee.views import EmployeeLoginAPI
from api.employee.views import UpdateEmployeeAPI
from api.employee.views import EmployeeLogoutAPI
from api.employee.views import RemoveEmployeeAPI
from api.employee.views import EmployeeDetailsAPI
from api.employee.views import ChangePasswordAPI

employee_blueprint = Blueprint('employee_blueprint_v1', __name__)
api = Api(employee_blueprint, prefix='/api/v1/employee')

api.add_resource(EnrollEmployeeAPI, '/enroll', strict_slashes=False)
api.add_resource(EmployeeLoginAPI, '/login', strict_slashes=False)
api.add_resource(UpdateEmployeeAPI, '/update', strict_slashes=False)
api.add_resource(ChangePasswordAPI, '/reset-pass', strict_slashes=False)
api.add_resource(EmployeeLogoutAPI, '/logout', strict_slashes=False)
api.add_resource(RemoveEmployeeAPI, '/remove', strict_slashes=False)
api.add_resource(EmployeeDetailsAPI, '/details', strict_slashes=False)
