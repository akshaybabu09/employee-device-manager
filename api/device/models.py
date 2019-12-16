from api import db
from api.employee.models import fetch_random_employee
from api.utils.constants import DEVICE_INFO, EMPLOYEE_TABLE


class Device(db.Model):

    __tablename__ = DEVICE_INFO

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    assigned_employee_id = db.Column(db.String, db.ForeignKey('{}.id'.format(EMPLOYEE_TABLE)))
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    device_id = db.Column(db.String, unique=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get('uuid')
        self.name = kwargs.get('name')
        self.assigned_employee_id = kwargs.get('assigned_employee_id')
        self.manufacturer = kwargs.get('manufacturer')
        self.model = kwargs.get('model')
        self.device_id = kwargs.get('device_id')

    @property
    def serialize(self):
        return {
            "device_id": self.device_id,
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
        }

    @staticmethod
    def assign_a_random_employee():
        return fetch_random_employee()


def fetch_devices_from_emp_uuid(emp_uuid):
    query_set = Device.query.filter(
        Device.assigned_employee_id == emp_uuid,
        Device.is_deleted == False
    ).all()
    device_details = {}
    for device in query_set:
        device_detail = device.serialize
        device_details[device.device_id] = device_detail
    return device_details
