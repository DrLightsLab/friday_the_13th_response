from flask import Flask, Blueprint
from .resources import blueprint as api_blueprint
from .foo import blueprint as foo_blueprint
import os

__all__ = ('create_app',)

# add blue prints here:
BLUEPRINTS = (
    api_blueprint,
    foo_blueprint
)

def create_app():
    app = Flask('friday_the_13th_response')
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

    
    # register blueprints
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
    