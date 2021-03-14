''' handling errors for the api rest '''
from . import errors


@errors.app_errorhandler(404)
def not_found(e):
    ''' Function where url mapping problems will be handled and not found, it will
    return its status and message. '''
    return {"Message": "Not found the path, please go to the home"}, 404
