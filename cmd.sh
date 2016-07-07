#!/bin/bash
FLASKAPP=waypointapp.py
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running dev server"
    exec python /app/$FLASKAPP
else
    echo "Running production server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/$FLASKAPP --callable app --stats 0.0.0.0:9191
fi

