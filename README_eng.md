# API REST - Docker flask

This project is a service that is able to recognize the longest palindrome within a text string, this will have security protocols using TOKENS. It also has a cache system that shows the last 10 palindrome words that have been searched by the api.

A palindrome is a string that when inverted is exactly the same as the original string.

```
    ana == palindromo
```

### project requirements

In order to execute the project, the following requirements must already be in place

- Docker
- Python == 3.9.2
- gcloud CLI
- git

# installation

In order to run the project locally, several steps are necessary.

1. Start by cloning the project.

```
git clone https://github.com/andresvanegas19/flask-docker-technical-test.git
```

2. It is necessary to have a google account and sign up for firebase services.
3. Create a web project, and after that go to project configuration to copy the following json and save it in a file named fbconfig.json
   ![](https://i.imgur.com/WnZeTjf.png)
4. Then go to the Configuration part of the project to generate a key and with this you can communicate and validate the user tokens, when generating the key move the file to src and rename it fbAdminConfig.json
   ![](https://i.imgur.com/8cZetFq.png)

The above steps were for user authentication.

5. For a good functioning of the enpoint /history (see below part of enpoints) it is necessary to create a db of redis to use it as db and to show the last results. To create a db go to the page https://redislabs.com where they will offer a db with a space of 6MB for free.

### DOCS - redis python

[redis](https://redislabs.com/lp/python-redis/)

6. Already when creating a redis db, the following environment variables must be set in an .env file with the information given by redislabs

```
export HOST=
export PORT_DB=
export PASSWORD=

```

![](https://i.imgur.com/J1vuMLe.png)

7. By following these steps you can now run the following command to run a container locally to test the REST API

```
docker-compose up --build -d api
```

if the container does not run you can see what problems are occurring by executing the following command

```
docker-compose logs -t -f --tail 10
```

### Estructura del proyecto

```
    cloudbuild.yaml     # For container deployment in GCP
    Dockerfile          # To create a container image
    docker-compose.yml  # Instrucciones de ejecucion del contenedor
    app.py              # Container execution instructions
    test/               # Van a traer todas las pruebas que se hicieron en la aplicación.
        ...
    resources/
        __init__.py
        auth.py          # contains logic for /api/tokens /api/signup
        ...
    common/
        __init__.py
        find_pal.py         # Functions that will help the structure
        ...
    ...
```
The common directory contain a set of helper functions to fulfill common needs across your application

# Construido con 🛠️

the following technologies are used.

- [ ] Flask
- [ ] firebase_admin
- [ ] flask_restful
- [ ] redis
- [ ] flask_cors
- [ ] pyrebase
- [ ] PyCryptodome
- [ ] jwt
- [ ] flask_swagger_ui

These technologies are used because you want to build a not so robust but persistent api.

# end-points

The entry points of the application will be as follows

```
GET    /api/signup
GET    /api/token
GET    /docs
GET    /
GET    /api/history
POST   /api/palindromo
```

## Descripcion

for more information you can find out at /docs
![](https://i.imgur.com/TN97pn2.png)

# testing

The following project ran the following tests to validate the proper functioning of the project.

```
python -m  src.test.test_largest_palindrome
```

# deployment

for easy deployment in GCP follow the steps at the beginning and go to the following link

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=github.com/andresvanegas19/flask-docker-technical-test)

If you have gcloud CLI run the following command and then go to cloud run and run the container

```
gcloud builds submit --tag gcr.io/[id-proyecto]/gcp-api
```
