import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api import app, db, celery

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# App Register
from api.employee import employee_blueprint
from api.device import device_blueprint

app.register_blueprint(employee_blueprint)
app.register_blueprint(device_blueprint)


celery.conf.update(app.config)


@manager.command
def runserver():
    """ overriding the runserver command
    """
    app.run(host='0.0.0.0', port=8001, debug=True)


if __name__ == '__main__':
    manager.run()
