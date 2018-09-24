from flask import Flask, Blueprint
from flask_restplus import Api, Namespace, Resource
import os
import json

__all__ = ('create_app',)

stock_api = Namespace('stock')
article_api = Namespace('article')
alert_api = Namespace('alert')

@stock_api.route('/', strict_slashes=False)
class Stock(Resource):
    def get(self):
        "Returns json response from file stock.json"
        data = get_json('stock')
        return data

@article_api.route('/', strict_slashes=False)
class Article(Resource):
    def get(self):
        "Returns json response from article.json"
        data = get_json('article')
        return data

@alert_api.route('/', strict_slashes=False)
class Alert(Resource):
    def get(self):
        "Returns json response from alert.json"
        data = get_json('alert')
        return data

def create_app():
    app = Flask('friday_the_13th_response')
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

    blueprint = Blueprint('api', __name__, url_prefix='/jason')
    api = Api(blueprint)
    api.add_namespace(stock_api)
    api.add_namespace(article_api)
    api.add_namespace(alert_api)
    app.register_blueprint(blueprint)

    return app

def get_json(file):
    try:
        with open('./friday_the_13th_response/data/' + file + '.json', 'rb') as file:
            data = json.load(file)
            print(data)
    except Exception as e:
        data = {'error' : str(e), 'dir' : str(os.getcwd())}
    return data