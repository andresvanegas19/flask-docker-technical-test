''' this file is for routing the endpoints '''

from flask import Blueprint
routes = Blueprint('routes', __name__)
errors = Blueprint('errors', __name__)

# keep to end for avoid circular import
from .error import *
from .auth import *
from .palindrome import *
from .welcome import *

