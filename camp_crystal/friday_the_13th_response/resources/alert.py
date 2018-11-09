from flask_restplus import Namespace
from .base import Base

api = Namespace('alert')

@api.route('/', strict_slashes=False)
class Alert(Base):
    title = 'alert'
    "Returns json response from alert json file"
    pass
    