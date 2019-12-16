# Employee - Device Manager
A new device, upon enrolling, will be assigned to one of the employees. The details of the assigned device will be shared to the employee via email.


## Problem Statement

Whenever an employee is created he/she is allocated an EMPLOYEE_ID, for the inputs taken as FIRST_NAME, LAST_NAME, E_MAIL, and MOBILE_NUMBER.

Each employee can be assigned more that one device that is identified by an DEVICE_ID.

Create a flask app to replicate CRUD operations:
1. Create an Employee
2. Update Employee details
3. Create Device
4. Update Device Details
5. Assign a device to an employee

Whenever a device is assigned or unassigned send out the details of the same to the corresponding employee as an e-mail.

## Setup
```
git clone https://github.com/akshaybabu09/employee-device-manager.git
cd employee-device-manager
sudo apt-get update
sudo apt-get install python3.6
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Execution Flow
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
```

## Explanantion

### Operations that can be performed on the Employee are as follows:

#### 1. Enroll Employee
      URL: /api/v1/employee/enroll
      
      FIRST_NAME:
      LAST_NAME:
      CONTACT:
      EMAIL:
      
      A unique 6 digit EMPLOYEE_ID will be generated & the PASSWORD will be set as contact.

#### 2. Login Employee - JSON Web Tokens 
    URL: /api/v1/employee/login
    
    EMP_ID:
    PASSWORD:
    
    Receives a Token.

#### 3. Update Employee Details
    URL: /api/v1/employee/update
    Header: {access-token : <token received upon Login>
    
    CONTACT:
    EMAIL:
    ADDRESS:
    PINCODE:

#### 4. Display Details of All Employees
    URL: /api/v1/employee/details
    Header: {access-token : <token received upon Login>

#### 5. Display Details of an Employee
    URL: /api/v1/employee/
    Header: {access-token : <token received upon Login>

#### 6. Remove Employee
    URL: /api/v1/employee/remove
    Header: {access-token : <token received upon Login>
    
    EMP_ID:


### Operations that can be performed on Device are as follows:

#### 1. Enroll Device.
    URL: /api/v1/device/enroll
    Header: {access-token : <token received upon Login>
    
    NAME:
    MANUFACTURER:
    MODEL:
    DEVICE_ID:
    EMP_ID:
    
    Device ID should be unique. 
    Once the device is successfully enrolled the device details will be shared to the employee via Email.

#### 2. Update Device Details.
    URL: /api/v1/device/update
    Header: {access-token : <token received upon Login>
    
    NAME:
    MANUFACTURER:
    MODEL:
    DEVICE_ID:                               (To fetch the device object.)

#### 3. Display Details of all Devices.
    URL: /api/v1/device/details
    Header: {access-token : <token received upon Login>

#### 4. Display Details of a Device.
    URL: /api/v1/device/details?device_id=DEVICE_ID
    Header: {access-token : <token received upon Login>

#### 5. Remove Device
    URL: /api/v1/device/remove
    Header: {access-token : <token received upon Login>
    
    DEVICE_ID:
    
    Once the device is successfully removed (soft delete) the device details will be shared to the employee 
    via Email.


