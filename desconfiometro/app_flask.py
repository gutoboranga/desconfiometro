from flask import Flask
from flask_cors import CORS

from desconfiometro.blueprints.home import home_blueprint
from desconfiometro.blueprints.api import api_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(api_blueprint)
    CORS(app)
    return app
