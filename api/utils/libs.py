import datetime

import jwt

from api import app


def generate_token(emp):
    token = jwt.encode(
        {
            'emp_id': emp.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)

         },
        app.config['SECRET_KEY']
    )
    return token
