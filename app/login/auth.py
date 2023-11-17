from flask import Blueprint, render_template, request

users = {
    'username': 'password'
}

login_bp = Blueprint('login_bp', __name__, template_folder='../templates')

@login_bp.route('/')
def index():
    return render_template('login.html')

@login_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Autenticazione riuscita
        return "Login successo!"
    else:
        # Autenticazione fallita
        return "Credenziali errate, riprova."

