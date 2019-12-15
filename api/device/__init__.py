from flask import Blueprint
from flask_restful import Api

from api.device.views import EnrollDeviceAPI
from api.device.views import UpdateDeviceDetailsAPI
from api.device.views import DisplayDeviceDetailsAPI
from api.device.views import RemoveDeviceAPI

device_blueprint = Blueprint('device_blueprint_v1', __name__)
api = Api(device_blueprint, prefix='/api/v1/device')

api.add_resource(EnrollDeviceAPI, '/enroll', strict_slashes=False)
# api.add_resource(EmployeeLoginAPI, '/login', strict_slashes=False)
api.add_resource(UpdateDeviceDetailsAPI, '/update', strict_slashes=False)
# api.add_resource(EmployeeLogoutAPI, '/logout', strict_slashes=False)
api.add_resource(RemoveDeviceAPI, '/remove', strict_slashes=False)
api.add_resource(DisplayDeviceDetailsAPI, '/details', strict_slashes=False)
