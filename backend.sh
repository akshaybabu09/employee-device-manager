##!/bin/bash
#NAME="backend"                                          # Name of the application
#PROJECT_DIR=~/loktra/au-backend
#USER=akshay
#GROUP=akshay
#NUM_WORKERS=5                                     # how many worker processes should Gunicorn spawn
#FLASK_APP=manage                     # WSGI module name
##FLASK_SOCKET=flask_sockets
#echo "Starting $NAME as `whoami`"
#
## Activate the virtual environment
#cd $PROJECT_DIR
#. ~/loktra/au-backend/venv/bin/activate
#export PYTHONPATH=$PROJECT_DIR:$PYTHONPATH

# Example aliases
export MAIL_USERNAME='testmail.loktra@gmail.com'
export MAIL_PASSWORD='testmail*1243'
export APP_SETTINGS="config.ProductionConfig"
export DATABASE_NAME='manager_db'
export DATABASE_USER='manager'
export DATABASE_PASSWORD='manager*1243'
export DATABASE_HOST='localhost'
export DATABASE_URL="postgresql://manager:manager*1243@localhost:5433/manager_db"