# API REST

un servicio que sea capaz de reconocer el palíndromo más largo dentro de una cadena de texto

las instrucciones de compilación, instalación, despliegue y uso de la API. También se deberá incluir la documentación de la API REST, endpoints, payloads y responses.

API REST
servicios de integración
pruebas unitarias y demás
componentes
artefactos de software

# iniciar

```
docker-compose up --build -d
```

if the container doesnt run please execute this commands
```
docker-compose logs -t -f --tail 10
```
requests==2.11.1

# Pre-requisitos 📋]

Puedes ver los requisitos de que se usan para desarrollar este proyecto

### instalar

para instalar la aplicacion es necesario correr los siguientes pasos

---

# Construido con 🛠️

se usa las siguientes tecnologias.

marshmallow
validate, serialize, and deserialize data.

---

### structure

```
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
```

# end-points

para ver que endpoints tiens

![](https://i.imgur.com/cN5lRqY.png)

# testing

for running testing in the file use

```
python -m  src.test.test_largest_palindrome
```
# deployment

For fast deployment use the following botton
but you need into the console paste the env variables and the firebase files


[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=github.com/andresvanegas19/flask-docker-technical-test)


if you use the CLI it will be more esily
run this:
```
gcloud builds submit --tag gcr.io/docker-tecninca/gcp-api
```

