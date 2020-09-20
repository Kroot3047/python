from Block import *

class Blockchain:

    def __init__(self, diff=2): # miningRD=100
        self.difficulty = diff
        self.chain = []
        self.__create_genesis_block()

    def __create_genesis_block(self):
        genesis_block = Block('0'*64)
        """nonce_ , proof = self.proof_of_work(genesis_block)
        genesis_block.nonce = nonce_
        self.chain.append(genesis_block)"""
        self.add_block(genesis_block)
        return genesis_block

    #@property
    def last_block(self):
        return self.chain[-1]

    # exclude genesis block    
    def size(self):
        return len(self.chain)-1

    def add_block(self, block): #block.previous_hash!='0'*(256/4) and 
        if block.previous_hash!='0'*64 and self.last_block().compute_hash() != block.previous_hash:
            return False

        block.nonce = self.mine(block)
        self.chain.append(block)
        return True

    def mine(self, block):
        nonce_ , proof = self.proof_of_work(block)
        if not self.is_valid_proof(block, proof):
            return False
        return nonce_

    def proof_of_work(self, block):
        nonce_ = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            nonce_ += 1
            computed_hash = block.compute_hash()

        return nonce_ , computed_hash

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * self.difficulty) and block_hash == block.compute_hash())


    #@classmethod
    def check_chain_validity(self):

        for i in range(1, len(self.chain)):
            block_down = self.chain[i-1]
            block_up = self.chain[i]
            if(block_down.compute_hash() != block_up.previous_hash):
                print("error in hash block N° : ",block_up.id)
                return False
            if(block_up.time.timestamp() < block_down.time.timestamp()):
                print("error in time of block N° : ",block_up.id)
                return False

        return True

