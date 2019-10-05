from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
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