from api import db
from api.device.models import Device
from api.employee.models import fetch_employee_from_emp_id, fetch_employee_from_uuid
from api.employee.services import generate_id


def enroll_device(emp, device_data):
    device = Device(
        uuid=generate_id(),
        name=device_data.get('name'),
        manufacturer=device_data.get('manufacturer'),
        model=device_data.get('model'),
        device_id=device_data.get('device_id'),
        assigned_employee_id=emp.id
    )

    db.session.add(device)
    db.session.commit()


def check_for_device_id(device_id):
    device = Device.query.filter(
        Device.device_id == device_id,
        Device.is_deleted == False
    ).first()
    if device:
        return True
    return False


def update_device_details(device_details):
    device = Device.query.filter(Device.device_id == device_details.get('device_id')).first()
    device.manufacturer = device_details.get('manufacturer', device.manufacturer)
    device.model = device_details.get('model', device.model)
    device.name = device_details.get('name', device.name)
    db.session.add(device)
    db.session.commit()


def fetch_device_details():
    query_set = Device.query.filter(
        Device.is_deleted == False
    ).all()
    device_details = {}
    for device in query_set:
        device_detail = device.serialize
        device_detail["assigned_employee"] = fetch_employee_from_uuid(device.assigned_employee_id)

        device_details[device.device_id] = device_detail
    return device_details


def remove_device(device_id):
    device = Device.query.filter(
        Device.device_id == device_id
    ).first()

    device.is_deleted = True
    db.session.add(device)
    db.session.commit()