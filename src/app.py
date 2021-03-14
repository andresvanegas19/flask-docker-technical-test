''' where the api start and asign the endpoints '''
from flask_cors import CORS
from flask import Flask, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

from .resources import *
from .extensions import drive_redis, firebase

app = Flask(__name__)

# initiating connection with redis
drive_redis.init_app(app)

# initiating connection with firebase
firebase.init_app(app)


app.register_blueprint(routes)
app.register_blueprint(errors)


# configurate the CORS
CORS(app, supports_credentials=True)
# CORS(app)
# cors = CORS(app, resource={
#     r"/*": {
#         "origins": "*"
#     }
# })

# init the docs
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python-Flask-REST"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
