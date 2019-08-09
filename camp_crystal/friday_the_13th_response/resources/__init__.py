from flask import Blueprint
from flask_restplus import Api
from .stock import api as api_stock
from .article import api as api_article
from .alert import api as api_alert
from .inventory import api as api_inventory

blueprint = Blueprint('api', __name__, url_prefix='/jason')
api = Api(blueprint)

# Add name space here:
api.add_namespace(api_stock)
api.add_namespace(api_article)
api.add_namespace(api_alert)
api.add_namespace(api_inventory)