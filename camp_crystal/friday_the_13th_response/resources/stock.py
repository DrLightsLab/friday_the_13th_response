from flask_restplus import Namespace
from .base import Base

api = Namespace('stock')

@api.route('/', strict_slashes=False)
class Stock(Base):
    title = 'stock'
    "Returns json response from stock json file"
    pass