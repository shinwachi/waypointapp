#!/bin/bash
FLASKAPP=waypointapp.py
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running dev server"
    exec python /app/$FLASKAPP &
	echo "running jupyter"
	cd /data
	exec sh -c 'jupyter notebook --port=8888 --ip=0.0.0.0 --no-browser'

else
    echo "Running production server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/$FLASKAPP --callable app --stats 0.0.0.0:9191
fi


