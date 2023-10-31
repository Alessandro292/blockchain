import json
import os

from flask import Blueprint, jsonify

swagger_bp = Blueprint('swagger_bp', __name__, template_folder='../../swagger')


@swagger_bp.route('/swagger.json')
def swagger():
    with open('swagger/swagger.json', 'r') as f:
        return jsonify(json.load(f))
