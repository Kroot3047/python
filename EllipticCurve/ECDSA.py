class ECDSA(object):
    def __init__(self, curve, generator, order):
        self.curve = curve
        self.G = generator
        self.n = order

    def sign(self, msghash, privkey):
        msg = bytes_to_int(msghash)
        k = randint(1, self.n - 1)
        i, j = k * self.G
        r = i % self.n
        s = (mod_inverse(k, self.n) * (msg + r * privkey)) % self.n
        return r, s