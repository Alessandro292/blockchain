import json

from flask import Blueprint, jsonify, logging

route_logger = logging.getLogger('route_logger')

swagger_bp = Blueprint('swagger_bp', __name__, template_folder='../../swagger')

@swagger_bp.route('/swagger.json')
def swagger():
    route_logger.info('Request to /api/swagger.json endpoint')
    with open('swagger/swagger.json', 'r') as f:
        return jsonify(json.load(f))
