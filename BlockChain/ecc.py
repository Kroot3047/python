from fastecdsa import curve, ecdsa, keys
from hashlib import sha384

m = "a message to sign via ECDSA"  # some message

"""
curve = Curve(
    name,  # (str): The name of the curve
    p,  # (long): The value of p in the curve equation.
    a,  # (long): The value of a in the curve equation.
    b,  # (long): The value of b in the curve equation.
    q,  # (long): The order of the base point of the curve.
    gx,  # (long): The x coordinate of the base point of the curve.
    gy,  # (long): The y coordinate of the base point of the curve.
    oid  # (str): The object identifier of the curve (optional).
)
"""

''' use default curve and hash function (P256 and SHA2) '''
private_key = keys.gen_private_key(curve.P256)
public_key = keys.get_public_key(private_key, curve.P256)
# standard signature, returns two integers
r, s = ecdsa.sign(m, private_key)
#encoded = DEREncoder.encode_signature(r, s)
#decoded_r, decoded_s = DEREncoder.decode_signature(encoded)
# should return True as the signature we just generated is valid.
valid = ecdsa.verify((r, s), m, public_key)

''' specify a different hash function to use with ECDSA '''
r, s = ecdsa.sign(m, private_key, hashfunc=sha384)
valid = ecdsa.verify((r, s), m, public_key, hashfunc=sha384)


''' specify a different curve to use with ECDSA '''
private_key = keys.gen_private_key(curve.P224)
public_key = keys.get_public_key(private_key, curve.P224)
r, s = ecdsa.sign(m, private_key, curve=curve.P224)
valid = ecdsa.verify((r, s), m, public_key, curve=curve.P224)

''' using SHA3 via pysha3>=1.0b1 package '''
import sha3  # pip install [--user] pysha3==1.0b1
from hashlib import sha3_256
private_key, public_key = keys.gen_keypair(curve.P256)
r, s = ecdsa.sign(m, private_key, hashfunc=sha3_256)
valid = ecdsa.verify((r, s), m, public_key, hashfunc=sha3_256)
