from flask import Blueprint
from flask_restful import Api

from api.employee.controllers.display_employee_details import EmployeeDetailsAPI
from api.employee.controllers.all_employee_details import AllEmployeeDetailsAPI
from api.employee.controllers.employee_login import EmployeeLoginAPI
from api.employee.controllers.enroll_employee import EnrollEmployeeAPI
from api.employee.controllers.remove_employee import RemoveEmployeeAPI
from api.employee.controllers.update_employee_details import UpdateEmployeeAPI

employee_blueprint = Blueprint('employee_blueprint_v1', __name__)
api = Api(employee_blueprint, prefix='/api/v1/employee')

api.add_resource(EnrollEmployeeAPI, '/enroll', strict_slashes=False)
api.add_resource(EmployeeLoginAPI, '/login', strict_slashes=False)
api.add_resource(UpdateEmployeeAPI, '/update', strict_slashes=False)
api.add_resource(RemoveEmployeeAPI, '/remove', strict_slashes=False)
api.add_resource(AllEmployeeDetailsAPI, '/details', strict_slashes=False)
api.add_resource(EmployeeDetailsAPI, '/', strict_slashes=False)
