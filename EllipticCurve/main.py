
import hashlib

import numpy as np
import matplotlib.pyplot as plt

from EllipticCurve import EllipticCurve
from ECC import ECC
from Point import Point 
from Point import Inf

#from ECDSA import ECDSA 		


		
#P = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
#A = 0
#B = 7
#GX = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
#GY = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
#G = (GX, GY)
#N = 0XFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141




		

if __name__ == "__main__":
    
    a = 2; b = -2; p = 31; # Point(4,16);
    a = 8; b = 7; p = 11;  # Point(1,4);
    a = 1; b = 4; p = 13;  # Point(0,2);
    a = 1; b = 2; p = 7;  # Point(1,2);
    a = 1; b = 1; p = 7; # Point(4,16);
    curve = EllipticCurve(a, b, p);
    print(curve.tostring());
    
    
    n = curve.MaxOrder();
    generator = curve.PmaxOrder();
    print("generator : "+str(generator));
    ecc = ECC(curve, generator, n); 
    
    
    # chiffrement
    m = Point(curve, 0, 1);
    cipher = ecc.encrypt(m);
    print("Crypt m"+str(m)+" --- { "+str(cipher[0])+" , "+str(cipher[1])+" }");

                

    # dechiffrement
    mm = ecc.decrypt(cipher);
    print("Decrypt mm "+str(mm));    
    
    
    xs = [];
    ys = [];
    for pp in curve.pointsGroup:
        #if (not isinstance(pp, Inf)):
        xs.append(pp.x); 
        ys.append(pp.y); 
    
    t = np.arange(-5., 5., 0.2)
    plt.plot(t*t, t**3+a*t+b , xs, ys, 'r+'); # , 'r+' ro
    plt.axhline(0, color='black');
    plt.axvline(0, color='black');    
    plt.title(curve.tostring());
    plt.show()    
    
    
#    mystring = input('Enter String to hash: ')
#    # Assumes the default UTF-8
#    hash_object = hashlib.md5(mystring.encode());
#    print("md5("+mystring+"): "+str(hash_object.hexdigest()));
    

    