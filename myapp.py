import logging
import logging.config

from flask import Flask

from app.routers.blockchain_api import blockchain_bp
from app.routers.hello_api import hello_bp

# Carica la configurazione del logging dal file di configurazione
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('blockcahinLogger')

# Define app.
app = Flask(__name__)
app.register_blueprint(hello_bp)
app.register_blueprint(blockchain_bp)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False



