#!/bin/sh

if [[ "$DEVELOPMENT" = "local" ]]; then
    FLASK_APP=./src/app.py FLASK_DEBUG=1 flask run -h 0.0.0.0 --port $PORT
else
    exec gunicorn --bind :$PORT src.app:app --workers 1 --threads 1 --timeout 60 --log-level debug
fi
