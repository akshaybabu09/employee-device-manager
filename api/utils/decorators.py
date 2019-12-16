from functools import wraps

import jwt
from flask import request, Response

from api import app
from api.employee.models import Employee
from api.utils.status_codes import UNAUTHORIZED


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'access-token' in request.headers:
            token = request.headers['access-token']

        if not token:
            return Response('Token is missing!', UNAUTHORIZED)

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Employee.query.filter_by(id=data['emp_id']).first()
        except:
            return Response('Token is invalid!', UNAUTHORIZED)

        return f(current_user, *args, **kwargs)

    return decorated
