''' where the api start and asign the endpoints '''

from flask import Flask, request, Blueprint
from firebase_admin import credentials, auth
import firebase_admin
import pyrebase
import json
from flask_restful import Api, Resource, url_for

app = Flask(__name__)
# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)

# connect to firebase
cred = credentials.Certificate("./fbAdminConfig.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


def check_token(f):
    ''' This function is for validated the information of the each request '''
    def wrap(*args, **kwargs):
        if not request.headers.get('authorization'):
            return {'Message': 'No token provided'}, 400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except Exception as e:
            print(e)
            return {'message': 'Invalid token provided.'}, 400
        return f(*args, **kwargs)
    return wrap


# class Auth(Resource):
#     @check_token
#     def get(self):
#         return {'task': 'Say "Hello, World!"'}

# @app.route('/api/palindromo/json')
# @check_token
# def get_palindrome_json():
#     return {'data': users}, 200


# registro
@app.route('/api/signup')
def signup():
    ''' function user registration that response the user and if happend a error
    throw a message '''
    # make a function to validate the email
    email = request.form.get('email')
    # make a function to validated the password
    password = request.form.get('password')

    if email is None or password is None:
        return {"error": "Missing emai or password"}, 400

    try:
        user = auth.create_user(email=email, password=password)
        return {
            "Message": "Successfully create user {user}".format(user=user.uid)
        }, 200
    except Exception as e:
        print(e)
        return {"Message": "Error creating user"}, 400


# api.add_resource(Auth, '/task')

# app.register_blueprint(api_bp)


@app.route('/api/token')
def token():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except Exception as e:
        print(e)
        return {"Message": "There was an error"}, 400


if __name__ == '__main__':
    app.run(debug=True)
