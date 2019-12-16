from flask import Blueprint
from flask_restful import Api

from api.device.controllers.display_device_details import DisplayDeviceDetailsAPI
from api.device.controllers.enroll_device import EnrollDeviceAPI
from api.device.controllers.remove_device import RemoveDeviceAPI
from api.device.controllers.update_device_details import UpdateDeviceDetailsAPI

device_blueprint = Blueprint('device_blueprint_v1', __name__)
api = Api(device_blueprint, prefix='/api/v1/device')

api.add_resource(EnrollDeviceAPI, '/enroll', strict_slashes=False)
api.add_resource(UpdateDeviceDetailsAPI, '/update', strict_slashes=False)
api.add_resource(RemoveDeviceAPI, '/remove', strict_slashes=False)
api.add_resource(DisplayDeviceDetailsAPI, '/details', strict_slashes=False)
