# Use the slim for a small docker
FROM python:3.8-slim

# to set the working for the api
RUN mkdir /api

# add independecies and instilling
ADD requirements.txt /api/
RUN pip install -r --no-cache-dir requirements.txt

COPY ./src/fbAdminConfig.json /api/fbAdminConfig.json
COPY ./src/fbconfig.json /api/fbconfig.json
COPY ./src/.env /api/.env

RUN source /api/.env

COPY ./src /api

WORKDIR /api

# CMD python manage.py makemigrations \
# && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

