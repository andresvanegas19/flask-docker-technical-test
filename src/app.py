''' where the api start and asign the endpoints '''

from flask import Flask, request
from firebase_admin import credentials, auth
import firebase_admin
import pyrebase
import json

app = Flask(__name__)

# connect to firebase
cred = credentials.Certificate("./fbAdminConfig.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


users = [{'uid': 1, 'name': 'Noah Schairer'}]

def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'Message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap


@app.route('/api/userinfo')
def userinfo():
    return {'data': users}, 200


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
    except Exception, e:
        print(e)
        return {"Message": "Error creating user"}, 400


@aap.route('/api/token')
def token():
    email = request.form.get('email')
    password = request.form.get("password")
    try:
        jwt = user['idToken']
        user = pb.auth().sign_in_with_email_and_password(email, password)
        return {'token': jwt}, 200
    except Exception, e:
        print(e)
        return {"Message": "There was an error"}, 400



if __name__ == '__main__':
    app.run(debug=True)
