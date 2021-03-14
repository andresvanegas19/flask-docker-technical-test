import redis
from os import environ
from firebase_admin import credentials, auth
import firebase_admin
import pyrebase
import json


class ConRedis:
    ''' This is for make a straightforward way for make a connection
    and manage connection with redis '''

    def __init__(self):
        self.app = None
        self.driver = None

    def init_app(self, app):
        ''' for init the conection and en '''
        self.app = app
        self.connection()

    def connection(self):
        ''' This method is to make a connection between the app and
        he connection between redis '''
        try:
            self.driver = redis.Redis(
                host=environ.get('HOST'),
                db=0,
                port=environ.get('PORT_DB'),
                password=environ.get('PASSWORD'),
            )
        except Exception as e:
            print(e)

        return self.driver

    def get_db(self):
        ''' This is for get the driver and can make request '''
        if not self.driver:
            return self.connect()
        return self.driver

# connect to firebase


class FirebaseAuth:
    ''' this is for making a connection with firebase and persist in the whole
    application '''
    cred = credentials.Certificate("./src/fbAdminConfig.json")
    # _firebase = firebase_admin.initialize_app(cred)
    # _pb = pyrebase.initialize_app(json.load(open('./src/fbconfig.json')))

    def __init__(self):
        self.app = None
        self.firebase = None
        self.pb = None

    def init_app(self, app):
        ''' for init the conection of firebase '''
        self.app = app
        self.connection_firebase()

    def connection_firebase(self):
        ''' This method is to make a connection with firebase'''
        self.firebase = firebase_admin.initialize_app(self.cred)
        self.pb = pyrebase.initialize_app(
            json.load(open('./src/fbconfig.json')))
        return self.pb

    def get_admin(self):
        ''' This is for get the driver and can make request '''
        if not self.pb:
            return self.connection_firebase()
        return self.pb
