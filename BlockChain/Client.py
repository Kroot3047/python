
import json
import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:

	counter_ = 0

	def __init__(self):
		self.id = Client.counter_
		self.private_key = RSA.generate(1024, Crypto.Random.new().read)
		self.public_key = self.private_key.publickey()
		Client.counter_ += 1

	#@property
	def identity(self):
		return binascii.hexlify(self.public_key.exportKey(format='DER')).decode('ascii')







	def __dict__(self):
		#return collections.OrderedDict({
		return {
            'id': self.id,
            'private_key': binascii.hexlify(self.private_key.exportKey(format='DER')).decode('ascii'),
            'public_key': binascii.hexlify(self.public_key.exportKey(format='DER')).decode('ascii'),
            'identity' : self.identity()
            }#)

	def __str__(self):
		str_ = "Client [ "+json.dumps(self.__dict__(), sort_keys=True)+" ]"
		return str_



"""
client1 = Client()
print (client1.public_key.exportKey('PEM'))
"""
