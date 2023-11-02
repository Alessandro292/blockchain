import datetime
import json
import hashlib
import logging

blockchain_logger = logging.getLogger('blockchainLogger')


class Blockchain:
    """
    Info: class that implements a blockchain
    """

    def __init__(self):
        """
        Info : init a blockchain with the first block
        """

        self.__chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        """
        Info: creates a new block within the blockchain

        Args:
            proof (int): block proof.
            previous_hash (str): previous block hash.

        Returns:
            dict: new block created.
        """

        block = {
            'index': len(self.__chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        blockchain_logger.info(f'New block created. Block index equal to: {len(self.__chain) + 1}')
        self.__chain.append(block)
        return block

    def get_chain(self):
        """
        Info: return the entire blockchain
        """
        return self.__chain

    def get_previous_block(self):
        """
        Info: return the last block
        """
        return self.__chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Info: Runs the proof of work to generate a new proof

        Args:
            previous_proof (int): the proof of the previous block

        Returns:
            int: the new generated proof
        """
        new_proof = 1
        check_proof = False
        blockchain_logger.info(f'Try to find new proof of work')
        while check_proof is False:
            hash_operation = hashlib \
                .sha256(str(new_proof ** 2 - previous_proof ** 2).encode()) \
                .hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        blockchain_logger.info(f'Found new proof of work equal to: {new_proof}')
        return new_proof

    def hash(self, block):
        """
        Info: compute the hash of the provided block

        Args:
            block (dict): the block from which to calculate the hash

        Returns:
            str: block hash
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        blockchain_logger.info(f"Hash of the block with index {block['index']} calculate")
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        """
        Info: checks if the provided chain is valid

        Args:
            chain (list): The chain to verify

        Returns:
            bool: True if the chain is valid, otherwise False.
        """

        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                blockchain_logger.warning(f"Previous hash of block {block_index} is not equal"
                                          f"to the hash of the previous block {block_index-1}")
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib \
                .sha256(str(proof ** 2 - previous_proof ** 2).encode()) \
                .hexdigest()
            if hash_operation[:4] != '0000':
                blockchain_logger.warning("Hash is greater than four leading zeros")
                return False
            previous_block = chain[block_index]
            block_index += 1
        blockchain_logger.info(f'Chain is valid')
        return True
