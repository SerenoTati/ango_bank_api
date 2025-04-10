from flask import Flask

from src.endpoint.rates_endpoint import rate_endpoint_blueprint

app = Flask(__name__)
app.register_blueprint(rate_endpoint_blueprint)
if __name__ == '__main__':
    app.run(debug = True, port=8000, host='localhost')

