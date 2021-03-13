#!/bin/sh
FLASK_APP=./src/app.py flask run -h 0.0.0.0 --port $PORT
