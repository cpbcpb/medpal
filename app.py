from flask import Flask
import nexmo

client = nexmo.Client(key='7d3b3494', secret='vMF3mb7GNxMMDt9s')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    client.send_message({
        'from': '15859357147',
        'to': '18134849281',
        'text': 'Hello from Nexmo',
    })
    return 'HOMEPAGE AND LOGIN (Doesnt need to be extravagant'

@app.route('/signup', methods=["GET"])
def signup():
    return 'SIGNUP VIEW (This is not necessary)'

@app.route('/pharmacy', methods=["GET"])
def pharmacy():
    return 'PHARMACY VIEW'

@app.route('/delivery/map', methods=["GET"])
def map():
    return 'DELIVERY MAP VIEW'

@app.route('/delivery/deliver', methods=["GET"])
def deliver():
    return 'DELIVERY CONFIRMATION VIEW'

if __name__ == "__main__":
    app.run(debug=True)