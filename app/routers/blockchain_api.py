import logging
from uuid import uuid4

from flask import Blueprint, jsonify, request

from app.instances.blockchain import Blockchain

route_logger = logging.getLogger('route_logger')

blockchain_bp = Blueprint('blockchain_bp', __name__)

blockchain = Blockchain()

node_address = str(uuid4()).replace('-', '')


@blockchain_bp.route("/mine-block", methods=['GET'])
def mine_block():
    try:
        route_logger.info('Request to /api/mine-block endpoint')

        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        blockchain.add_transactions(sender=node_address, receiver='Impa', amount=10)
        block = blockchain.create_block(proof=proof, previous_hash=previous_hash)

        response = {'message': 'Congratulations! You just mined a block.',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash'],
                    'transactions': block['transactions']}

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
                    'length': len(blockchain.get_chain())}
        return jsonify(response), 200
    except Exception as e:
        route_logger.error(f'Error in get_chain: {e}')
        response = {'error': 'Blockchain is not reachable.'}
        return jsonify(response), 500


# Checking if the Blockchain is valid
@blockchain_bp.route('/is-valid', methods=['GET'])
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


@blockchain_bp.route('/add-transaction', methods=['POST'])
def add_transaction():
    try:
        route_logger.info('Request to /api/add-transaction')
        json_data = request.get_json()

        # Check if the required keys are present in the JSON data
        transaction_keys = ['sender', 'receiver', 'amount']
        if not all(key in json_data for key in transaction_keys):
            return jsonify({'error': "Missing key value"}), 400

        # Attempt to add the transaction to the blockchain
        index = blockchain.add_transactions(sender=json_data['sender'],
                                            receiver=json_data['receiver'],
                                            amount=json_data['amount'])

        response = {'Message': f'This transaction will be added to Block {index}'}
        return jsonify(response), 201

    except Exception as e:
        # Handle exceptions (e.g., invalid JSON, blockchain operation failure)
        error_message = f"Error processing the transaction: {e}"
        route_logger.error(error_message)
        return jsonify({'error': error_message}), 500


@blockchain_bp.route('/connect-node', methods=['POST'])
def connect_node():
    try:
        route_logger.info('Request to /api/connect-node')
        json_data = request.get_json()
        nodes = json_data.get('nodes')

        # Check if the 'nodes' key is present in the JSON data
        if nodes is None:
            return jsonify({'error': "No nodes provided"}), 400

        # Attempt to add the nodes to the blockchain
        for node in nodes:
            blockchain.add_nodes(address=node)

        response = {
            'message': 'All nodes are connected. Impaoin Blockchain is composed of the following nodes:',
            'total_nodes': list(blockchain.nodes)
        }
        return jsonify(response), 201

    except Exception as e:
        # Handle exceptions (e.g., invalid JSON, blockchain operation failure)
        error_message = f"Error connecting nodes: {e}"
        route_logger.error(error_message)
        return jsonify({'error': error_message}), 500


@blockchain_bp.route('/replace-chain', methods=['GET'])
def replace_chain():
    try:
        route_logger.info('Request to /api/replace-chain')

        # Attempt to replace the blockchain chain
        is_chain_replaced = blockchain.replace_chain()

        if is_chain_replaced:
            response = {
                'message': 'The nodes had different chains, so the chain was replaced by the longest',
                'new_chain': blockchain.get_chain()
            }
        else:
            response = {
                'message': 'All good. The chain is the longest one',
                'new_chain': blockchain.get_chain()
            }

        return jsonify(response), 200

    except Exception as e:
        # Handle exceptions (e.g., blockchain operation failure)
        error_message = f"Error replacing the chain: {e}"
        route_logger.error(error_message)
        return jsonify({'error': error_message}), 500
