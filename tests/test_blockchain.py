import datetime
import hashlib

from unittest.mock import MagicMock

# Mock logger
blockchain_logger = MagicMock()


def test_create_block(blockchain):
    proof = 1
    previous_hash = "0"
    block = blockchain.create_block(proof, previous_hash)
    assert isinstance(block, dict)
    assert 'index' in block
    assert 'timestamp' in block
    assert 'proof' in block
    assert 'previous_hash' in block

def test_get_chain(blockchain):
    chain = blockchain.get_chain()
    assert isinstance(chain, list)
    assert len(chain) == 1  # The genesis block should be present in the chain

def test_get_previous_block(blockchain):
    blockchain.create_block(proof=123, previous_hash="hash")
    previous_block = blockchain.get_previous_block()
    assert previous_block['proof'] == 123
    assert previous_block['previous_hash'] == "hash"

def test_proof_of_work(blockchain):
    previous_proof = 123
    new_proof = blockchain.proof_of_work(previous_proof)
    assert isinstance(new_proof, int)
    hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
    assert hash_operation[:4] == '0000'

def test_hash(blockchain):
    block = {
        'index': 1,
        'timestamp': str(datetime.datetime.now()),
        'proof': 123,
        'previous_hash': "hash",
    }
    block_hash = blockchain.hash(block)
    assert isinstance(block_hash, str)

