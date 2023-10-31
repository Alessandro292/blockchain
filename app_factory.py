from logging.config import fileConfig

from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from app.routers.blockchain_api import blockchain_bp
from app.routers.hello_api import hello_bp
from app.routers.swagger_api import swagger_bp

fileConfig('logging/logging.conf')

def create_app():

    # Define app.
    app = Flask(__name__)

    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    # Configure Api
    API_PREFIX = '/api'

    # Configure Swagger UI
    SWAGGER_URL = '/swagger'
    SWAGGER_JSON_URL = 'http://localhost:6969/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        SWAGGER_JSON_URL,
        config={
            'app_name': "Blockchain API"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(swagger_bp)

    app.register_blueprint(blockchain_bp, url_prefix=API_PREFIX)
    app.register_blueprint(hello_bp, url_prefix=API_PREFIX)

    return app



