from flask_restplus import Namespace
from .base import Base

api = Namespace('alert')

@api.route('/<string:title>', strict_slashes=False)
class Alert(Base):
    "Returns json response from alert json file"
    pass
    