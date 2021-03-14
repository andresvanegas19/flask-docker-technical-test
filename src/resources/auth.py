''' script for sign up for users and the users can see what tokens they have'''
from . import routes
from flask import request
from src.extensions import firebase
from firebase_admin import  auth

@routes.route('/api/signup', methods=["GET"])
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
        return {"Message": "Error creating user"}, 401


@routes.route('/api/token', methods=["GET"])
def token():
    ''' Function that will return the user's token so that he can use the endpoints,
     if the user does not have a token and has not registered, it will respond with
     a corresponding message.'''

    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = firebase.get_admin().auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except Exception as e:
        print(e)
        return {"Message": "There was an error"}, 400
