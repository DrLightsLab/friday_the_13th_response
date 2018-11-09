from flask import Flask, jsonify
from flask_restplus import Resource

class Base(Resource):
    def get(self):
        print('inbase')
        return jsonify(foo=f'{self.val}')