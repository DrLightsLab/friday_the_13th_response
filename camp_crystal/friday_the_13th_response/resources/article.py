from flask_restplus import Namespace
from .base import Base

api = Namespace('article')

@api.route('/<string:title>', strict_slashes=False)
class Article(Base):
    "Returns json response from article json file"
    pass
        

@api.route('/null/<string:title>', strict_slashes=False)
class Article(Base):
    "Returns json response from article-with-null json file"
    pass