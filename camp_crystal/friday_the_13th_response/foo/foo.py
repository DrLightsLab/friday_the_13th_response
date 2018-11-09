from flask_restplus import Namespace
from .base import Base

api = Namespace('foo')

@api.route('/', strict_slashes=False)
class Foo(Base):
    print(Base)
    val = 'foo'
    pass