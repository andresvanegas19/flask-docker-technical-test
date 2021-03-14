''' this script is for home enpoint '''

from . import routes


@routes.route('/', methods=["GET"])
def welcome():
    ''' this function return the welcome message with a 200 status'''
    welcome = "Please login in the enpoint /signup for use the api"
    return {"API-andres": welcome}, 200
