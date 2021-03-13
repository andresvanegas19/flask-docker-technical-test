''' where the api start and asign the endpoints '''

from flask import Flask, request, Blueprint
from firebase_admin import credentials, auth
import firebase_admin
import pyrebase
import json
from os import environ
import redis
from flask_restful import Api, Resource, url_for
from flask_cors import CORS
from .common.util import largest_palindrome

#  View function mapping is overwriting an existing endpoint function: wrap
from functools import wraps


app = Flask(__name__)
# configurate the CORS
CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

# connect to firebase
cred = credentials.Certificate("./fbAdminConfig.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

# connect to redis
host = environ.get('HOST')
port = environ.get('PORT')
password = environ.get('PASSWORD')
r = redis.Redis(host=host, port=port, db=0, password=password)


def check_token(f):
    ''' This function is for validated the information of the each request '''
    # avoid errors that  View function mapping is overwriting an existing endpoint function
    @wraps(f)
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


@app.route('/', methods=["GET"])
def history():
    # return {'data': 'users'}, 200
    welcome = "Please login in the enpoint /signup for use the api"
    return {"API-andres": welcome}, 200


@app.route('/api/history', methods=["GET"])
@check_token
def history_palindrome():
    values = r.keys('*')[:10]

    response = {}
    if len(values) < 10:
        lenght = len(values) - 1
    else:
        lenght = 10

    for i in range(lenght):

        response[str(i)] = values[i].decode("utf-8")

    return response, 200


@app.route('/api/palindromo', methods=["POST"])
@check_token
def get_palindrome_json():

    json_data = request.json
    if not "palindromo" in json_data:
        return {'Message': "missing the palindrome value"}, 400

    largest_p = largest_palindrome(json_data['palindromo'])
    if not largest_p:
        return {"Message": "There is not palindrome word in the string"}, 200

    response = {
        "palindrome_word": json_data['palindromo'],
        "largest_palindrome_word": largest_p
    }
    # save to db
    key = 'palindrome word {} => {}'.format(json_data['palindromo'], largest_p)
    try:
        r.set(key, largest_p)
    except Exception as e:
        print(e)

    return response, 200


# registro
@ app.route('/api/signup', methods=["GET"])
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


@app.route('/api/token', methods=["GET"])
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
