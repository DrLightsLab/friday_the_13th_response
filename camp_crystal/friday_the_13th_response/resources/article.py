from flask_restplus import Namespace
from .base import Base

api = Namespace('article')

@api.route('/', strict_slashes=False)
class Article(Base):
    title = 'article'
    "Returns json response from article json file"
    pass
        

@api.route('/null/', strict_slashes=False)
class Article(Base):
    title = 'article-with-null'
    "Returns json response from article-with-null json file"
    pass

@api.route('/discontinued/', strict_slashes=False)
class Article(Base):
    title = 'article-discontinued'
    "Returns json response from article-discontinued json file"
    pass