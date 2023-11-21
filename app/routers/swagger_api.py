import json
import logging
from flask import Blueprint, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from app.config.constants import SWAGGER_URL, SWAGGER_JSON_URL

route_logger = logging.getLogger('route_logger')

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_JSON_URL,
    config={'app_name': 'Blockchain API'}
)

swagger_bp = Blueprint('swagger_bp', __name__)

@swagger_bp.route('/swagger.json')
def swagger():
    route_logger.info('Request to /swagger.json endpoint')
    with open('../swagger/swagger.json', 'r') as f:
        return jsonify(json.load(f))
