import logging

from flask import Blueprint, render_template

route_logger = logging.getLogger('route_logger')

hello_bp = Blueprint('hello_bp', __name__, template_folder='../templates')


# Define route "/api".
@hello_bp.route("/")
def hello_world():
    route_logger.info('Request to /api/ endpoint')
    return "<p>Hello, World!</p>"


@hello_bp.route('/hello/')
@hello_bp.route('/hello/<name>')
def hello(name=None):
    route_logger.info(f'Request to /api/hello/{name} endpoint')
    return render_template('hello.html', name=name)
