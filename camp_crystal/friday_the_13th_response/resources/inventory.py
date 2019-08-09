from flask_restplus import Namespace
from .base import Base

api = Namespace('inventory')

@api.route('/', strict_slashes=False)
class Inventory(Base):
    title = 'inventory'
    "Returns json response from inventory json file"
    pass