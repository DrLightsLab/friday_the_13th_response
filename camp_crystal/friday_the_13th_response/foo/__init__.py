from flask import Blueprint
from flask_restplus import Api
from .foo import api as api_foo

blueprint = Blueprint('foo', __name__, url_prefix='/foo')
api = Api(blueprint)

api.add_namespace(api_foo)