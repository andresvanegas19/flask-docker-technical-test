FROM python:3.7-stretch

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# to set the working for the api
RUN mkdir /api

COPY . /api

WORKDIR /api

RUN pip install --no-cache-dir -r  requirements.txt

# RUN source /api/src/.env
# RUN . 
EXPOSE 5000
ENV PORT 5000


ENTRYPOINT [ "bash" ]

# CMD exec gunicorn --bind :$PORT main_v1:app --workers 1 --threads 1 --timeout 60
