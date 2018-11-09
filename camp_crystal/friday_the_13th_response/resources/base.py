from flask import Flask, send_from_directory
from flask_restplus import Resource
from ..conf import conf

class Base(Resource):
    def get(self):
        return send_from_directory(conf.STATIC_ROOT, f'{self.title}.json', cache_timeout=0)