from flask import Blueprint, render_template

hello_bp = Blueprint('hello_bp', __name__, template_folder='../templates')


# Define route "/api".
@hello_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@hello_bp.route('/hello/')
@hello_bp.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
