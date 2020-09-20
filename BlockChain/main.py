import os
#import Blockchain
from Blockchain import *
from Block import *
from Transaction import *
from Client import *
import json
import datetime
import time

print("##################### Blockchain System #####################")
"""
t = time.time()
time1 = datetime.datetime.now().timestamp()
time2 = datetime.datetime.now().timestamp()
print(t)
print(time1)
print(time2)
"""

client1 = Client()
client2 = Client()
t1 = Transaction(client1, client2, 5.0)
t2 = Transaction(client2, client1, 2.0)
#print (t1)
difficulty = 0
bc = Blockchain(difficulty) 
#print(bc.last_block()) #print(bc.chain[0])
block0 = Block(bc.last_block().compute_hash())
block0.addTrasaction(t1)
block0.addTrasaction(t2)
bc.add_block(block0)

for i, block_ in enumerate(bc.chain):
	blck = block_.__dict__()
	print("\n____________________________ Block N° ",str(blck['id'])," \n")
	print(json.dumps(blck, indent=4, sort_keys=True))

print("chain is valid? : ", bc.check_chain_validity())

"""
# the address to other participating members of the network
peers = set()
"""
os.system("pause")