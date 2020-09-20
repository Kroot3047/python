import hashlib
import json
import datetime

class Block:

    counter_ = 0 # len(self.chain) + 1

    def __init__(self, previous_block_hash): #verified_transactions = []
        self.id = Block.counter_
        self.time = datetime.datetime.now()
        self.transactions = [] 
        self.previous_hash = previous_block_hash
        #self.hash = None
        self.nonce = None
        Block.counter_ += 1

    def addTrasaction(self, transaction):
        """
        if (!transaction.fromAddress || !transaction.toAddress):
            print('Transaction must include from and to address')
            return False
        
        if (!transaction.isValid()):
            print('Cannot add invalid transaction to chain')
            return False
        """
        if (transaction.value <= 0):
            print('Transaction amount should be higher than 0')
            return False

        self.transactions.append(transaction)
        #print('transaction added: %s', transaction)
        return True
 

    def compute_hash(self):
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
        """
        key = hashlib.sha256()
        key.update(str(self.id).encode('utf-8'))
        key.update(str(self.time).encode('utf-8'))
        key.update(str(self.transactions).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()

    def __dict__(self):
        #return collections.OrderedDict({
        return {
            'id' : self.id,
            'time' : self.time.strftime("%m/%d/%Y, %H:%M:%S"),
            'transactions' : [tr_.__dict__() for tr_ in self.transactions ],
            'previous_hash' : self.previous_hash,
            'hash' : self.compute_hash(),
            'nonce' : self.nonce
            }#)

    def __str__(self):
        str_ = json.dumps(self.__dict__(), sort_keys=True)
        return " Block [ "+str_+" ]"


