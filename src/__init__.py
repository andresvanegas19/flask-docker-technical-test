# from flask import Flask
# from .admin.routes import admin
# from .api.routes import api
# from .website.routes import website
# from extensions import *
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.DevConfig')
#     # Initialise extensions
#     mongo.init_app(app)
#     with app.app_context():
#         app.register_blueprint(admin, url_prefix="/admin")
#         app.register_blueprint(api, url_prefix="/api")
#         app.register_blueprint(website)
#     return app