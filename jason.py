from flask import Flask
import json

app = Flask(__name__)

@app.route('/stock')
def stock():
    data = {}
    with open('stock.json', 'rb') as file:
        data = json.load(file)
        data = json.dumps(data)
    return data