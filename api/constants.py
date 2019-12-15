EMPLOYEE_TABLE = 'employee_table'
DEVICE_INFO = 'device_info'

DEVICE_ASSIGN = 'Device Assignment!!!'
DEVICE_UNASSIGN = 'Device Unassigning!!!'


def assign_mail_body(emp, device):
    DEVICE_ASSIGN_MAIL_BODY = """
    Hi """ + emp['first_name'] + """,
    
    You have been assigned with a new device!!!
    The details are as follows:
    
    Device Name:  """ + device.get('name') + """
    Device ID:  """ + device.get('device_id') + """
    Manufacturer:  """ + device.get('manufacturer') + """
    Model Name:  """ + device.get('model') + """
        
    Thank you!!!
    Have a wonderful day!!!
    """
    return DEVICE_ASSIGN_MAIL_BODY


def unassign_mail_body(emp, device):
    DEVICE_UNASSIGN_MAIL_BODY = """
    Hi """ + emp['first_name'] + """,
    
    You have been unassigned a device as it was deleted!!!
    The details are as follows:
    
    Device Name:  """ + device.get('name') + """
    Device ID:  """ + device.get('device_id') + """
    Manufacturer:  """ + device.get('manufacturer') + """
    Model Name:  """ + device.get('model') + """
        
    Thank you!!!
    Have a wonderful day!!!
    """
    return DEVICE_UNASSIGN_MAIL_BODY
