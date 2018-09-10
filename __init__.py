from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Ho World!"

@app.route("/foo")
def foo():
    return "Foo!"

@app.route("/stock")
def stock():
    try:
        with open('log.txt') as foo:
            foo.write('test')
            foo.close()
        #data = json.dumps({"uom": "YD", "imageUrl": null, "pricingData": [{"site": "4001","city": "INTERNET SITE","phone": "www.joann.com","onHands": "N/A","state": "","desc": ""},{"site": "DC01","city": "HUDSON","phone": "","onHands": "0.0","state": "OH","desc": "HUDSON DISTRIBUTION CENTER"}],"description": "RED/WHITE DOT","upc": "400111616013","thumbUrl": null,"article": "11161601","returnType": "S","message": null,"return": {}})
       #data = json.dumps(data)
       # with open('stock.json', 'rb') as file:
           # print(file)
    except Exception as e:
        with open('log.txt', 'w') as log:
            log.write(e)
            log.close()
        
#        data = json.load(file)
#        data = json.dumps(data)
    return data

if __name__ == "__main__":
    app.run()
