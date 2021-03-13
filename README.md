# API REST - Docker flask

Este proyecto es un servicio que sea capaz de reconocer el palíndromo más largo dentro de una cadena de texto, este tendra protocolos de seguridad utilizando TOKENS. Ademas tenga un sistema de cache donde muestre las utimas 10 palabras palindrome que se han buscado por la api.

un palíndromo es una cadena que al ser invertida es exactamente igual a la cadena original.

```
    ana == palindromo
```

# TOMAR EN CUENTA
Todo el codigo y la documentacion esta escrita en ingles por si es llegado a usar y tener mayor alcance del proyecto.

### requerimientos para el proyeto
Para poder ejecutar el proyecto es necesario que ya tenga instalado los siguientes requerimientos

- Docker
- Python == 3.9.2
- gcloud CLI
- git

# installation
Para poder corre el proyecto en local es necesario varios pasos.
1. Empieza clonando el proyecto.
```
git clone https://github.com/andresvanegas19/flask-docker-technical-test.git
```

2. Es necesario que se tenga una cuenta google y se registre en los servicios de firebase.
3. Crear un proyecto web, y despues de esto ir a configurancion del proyecto para copiar el siguiente json y guardarlo en un arhivo llamado fbconfig.json
![](https://i.imgur.com/WnZeTjf.png)
4. Luego ir a la parte de Configuración del proyecto para generar una llave y con esta se pueda comunicar y validar los tokens de los usuarios, al generar la llave move el archivo a src y renombrarlo fbAdminConfig.json
![](https://i.imgur.com/8cZetFq.png)

Los pasos anteriores eran para la autentificacion del usuario.


5. Para que haya un buen funcionamiento del enpoint /history (ver mas adelante parte de enpoints) es necesario crear un db de redis para usarlo como db y mostrar los ultimos resultados. Para crear un db irse a la pagina https://redislabs.com donde ofreceran un db con un espacio de 6MB gratis.

### DOCS - redis python
[redis](https://redislabs.com/lp/python-redis/)

6. ya al crear un db de redis se debe setear las siguientes variables de entorno en un archivo .env con la informacion dada de redislabs
```
export HOST=
export PORT_DB=
export PASSWORD=

```
![](https://i.imgur.com/J1vuMLe.png)

7. ya al seguir estos pasos ahora puede ejecutar el siguiente comando para correr un contenedor en local y poder probar la API REST
```
docker-compose up --build -d api
```
si el contenedor no corre puede ver cuales son los problemas que estan ocurriendo ejecutando el siguiente comando
```
docker-compose logs -t -f --tail 10
```

### Estructura del proyecto

```
    cloudbuild.yaml     # Para el deployment del contenedor en GCP
    Dockerfile          # Para crear una imagen del contenedor
    docker-compose.yml  # Instrucciones de ejecucion del contenedor
    app.py              # Contiene el inicio de la aplicacion
    resources/
        __init__.py
        foo.py          # contains logic for /Foo
        bar.py          # contains logic for /Bar
    common/
        __init__.py
        util.py         # Funciones que ayudaran a la estructura
```

# Construido con 🛠️

se usa las siguientes tecnologias.

Flask
firebase_admin
flask_restful
redis
flask_cors
pyrebase
PyCryptodome
jwt
flask_swagger_ui

Son usadas estas tecnologias porque se quiere construir una api no tan robusta pero que sea persistente.


# end-points
Los puntos de entrada de la aplicaion seran los siguientes
```
GET    /api/signup
GET    /api/token
GET    /docs
GET    /
GET    /api/history
POST   /api/palindromo
```
## Descripcion

## /api/singup
Este enpoint se puede probar ejecutando 
```
```


# testing

El siguinte proyecto corrio los siguientes test para validar el buen funcionamiento del proyecto.

```
python -m  src.test.test_largest_palindrome
```
# deployment

para facil deployment en GCP seguir los pasos del inicio y ir al siguiente link

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=github.com/andresvanegas19/flask-docker-technical-test)


Si tiene gcloud CLI ejecutar el siguiente comando y luego ir a cloud run y ejecutar el contenedor
```
gcloud builds submit --tag gcr.io/[id-proyecto]/gcp-api
```
