FROM python:3.7-stretch

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /api

WORKDIR /api

RUN pip install --no-cache-dir -r  requirements.txt

EXPOSE 5000
ENV PORT 5000

ENTRYPOINT [ "bash" ]
