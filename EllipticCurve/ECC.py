import random

class ECC(object):
    def __init__(self, curve, generator, order):
        self.curve = curve
        self.G = generator
        self.n = order
        self.privateKey = random.randint(0, order-1);
        self.publicKey = generator.mul(self.privateKey);

    def encrypt (self, m):
        k = random.randint(1, self.n - 1); #        k = random.randint(1, self.curve.p - 1); 
        aa = self.G.mul(k);
        bb = m.add(self.publicKey.mul(k));
        return [aa, bb];

    def decrypt (self, cipher):
        c = cipher[0].mul(self.privateKey);
        mm = cipher[1].add(c.neg());
        return mm;