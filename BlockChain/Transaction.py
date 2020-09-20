import Crypto # pycryptodome
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii
import datetime
import collections
import json

class Transaction:


    def __init__(self, sender, recipient, value):
        #self.NoTransaction = 
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.utcnow()

    def sign_transaction(self): #'You cannot sign transactions for other wallets!'
        h = Transaction.__compute_hash_SHA(self)#h = SHA.new(str(self.__dict__()).encode('utf8'))
        signer = PKCS1_v1_5.new(self.sender.private_key)
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    @staticmethod
    def verify_transaction_signature(transaction, signature):
        h = Transaction.__compute_hash_SHA(transaction)#SHA.new(str(transaction.__dict__()).encode('utf8'))
        verifier = PKCS1_v1_5.new(transaction.sender.public_key)
        return verifier.verify(h, binascii.unhexlify(signature))

    @staticmethod
    def __compute_hash_SHA(o):
        o_attrs = json.dumps({
            'sender': o.sender.identity(),
            'recipient': o.recipient.identity(),
            'value': o.value,
            'time' : o.time.strftime("%m/%d/%Y, %H:%M:%S")
            })
        h = SHA.new(str(o_attrs).encode('utf8'))
        return h

    def __dict__(self):
        #return collections.OdrderedDict({
        return {
            #'No': self.NoTransaction,
            'sender': self.sender.identity(),
            'recipient': self.recipient.identity(),
            'value': self.value,
            'time' : self.time.strftime("%m/%d/%Y, %H:%M:%S"),
            'signature' : self.sign_transaction()
            }#)

    def __str__ (self):
        #dict_.update({'signature' : self.sign_transaction()})
        str_ = json.dumps(self.__dict__(), sort_keys=True)
        return "Transaction [ "+str_+" ]"


"""
    def __getattr__(self, attr):
        return self.data[attr]


client1 = Client()
client2 = Client()
t1 = Transaction(client1, client2, 5.0)
print (t1)

signature = t1.sign_transaction()
print (signature)
isValidSignature = Transaction.verify_transaction_signature(t1, signature)
print(isValidSignature)

"""

