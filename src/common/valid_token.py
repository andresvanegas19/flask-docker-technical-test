#  View function mapping is overwriting an existing endpoint function: wrap
from functools import wraps
from flask import request
from firebase_admin import  auth

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
