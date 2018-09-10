from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Ho World!"

@app.route("/foo")
def foo():
    return "Foo!"

@app.route("/stock", methods=['GET'])
def stock():
    if(request.method == 'GET'):
        try:
            data = {}
            with open('log.txt', 'w') as foo:
                foo.write('test')
                foo.close()
            #data = json.dumps({"uom": "YD", "imageUrl": null, "pricingData": [{"site": "4001","city": "INTERNET SITE","phone": "www.joann.com","onHands": "N/A","state": "","desc": ""},{"site": "DC01","city": "HUDSON","phone": "","onHands": "0.0","state": "OH","desc": "HUDSON DISTRIBUTION CENTER"}],"description": "RED/WHITE DOT","upc": "400111616013","thumbUrl": null,"article": "11161601","returnType": "S","message": null,"return": {}})
            #data = json.dumps(data)
            with open('./data/stock.json', 'rb') as file:
                data = json.load(file)
                data = json.dumps(data)
        except Exception as e:
            with open('log.txt', 'w') as log:
                log.write(str(e))
                log.close()
        # return json.dumps(data)
        return data
    else:
        return 'This is a post dumbass'

if __name__ == "__main__":
    app.run()
