from flask import Flask

from src.endpoint.rates_endpoint import rate_endpoint_blueprint

app = Flask(__name__)
app.register_blueprint(rate_endpoint_blueprint)
