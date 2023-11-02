import logging

from flask import Blueprint, jsonify

from app.instances.blockchain import Blockchain

route_logger = logging.getLogger('route_logger')

blockchain_bp = Blueprint('blockchain_bp', __name__)

blockchain = Blockchain()

@blockchain_bp.route("/mine-block", methods=['GET'])
def mine_block():
    try:
        route_logger.info('Request to /api/mine-block endpoint')

        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof=proof, previous_hash=previous_hash)

        response = {'message': 'Congratulations! You just mined a block.',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}

        return jsonify(response), 200
    except Exception as e:
        route_logger.error(f'Error in is_valid: {e}')
        response = {'error': 'Error during the mining of the new block'}
        return jsonify(response), 500


@blockchain_bp.route("/get-chain", methods=['GET'])
def get_chain():
    try:
        route_logger.info('Request to /api/get-chain endpoint')
        response = {'chain': blockchain.get_chain(),
                    'lenght': len(blockchain.get_chain())}
        return jsonify(response), 200
    except Exception as e:
        route_logger.error(f'Error in get_chain: {e}')
        response = {'error': 'Blockchain is not reachable.'}
        return jsonify(response), 500

# Checking if the Blockchain is valid
@blockchain_bp.route('/is-valid', methods = ['GET'])
def is_valid():
    try:
        route_logger.info('Request to /api/get-chain endpoint')
        is_valid = blockchain.is_chain_valid(blockchain.get_chain())
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
        return jsonify(response), 200
    except Exception as e:
        route_logger.error(f'Error in is_valid: {e}')
        response = {'error': 'Error during validation.'}
        return jsonify(response), 500