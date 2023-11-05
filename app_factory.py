from logging.config import fileConfig
from os import path

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.config.config import config_dict
from app.config.constants import *
from app.routers.blockchain_api import blockchain_bp
from app.routers.hello_api import hello_bp
from app.routers.swagger_api import swagger_bp


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging', 'logging.conf')
fileConfig(log_file_path)

def create_app(config_name: str):
    app = Flask(__name__)

    selected_config = config_dict[config_name]
    app.config.from_object(selected_config)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        SWAGGER_JSON_URL,
        config={'app_name': 'Blockchain API'}
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(swagger_bp)
    app.register_blueprint(blockchain_bp, url_prefix=API_PREFIX)
    app.register_blueprint(hello_bp, url_prefix=API_PREFIX)

    return app


