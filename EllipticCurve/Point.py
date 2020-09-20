

class Point(object):
    """A point on a specific curve."""
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x % curve.p
        self.y = y % curve.p

        if not self.curve.has_point(x, y):
            raise ValueError('{} is not on curve {}'.format(self, self.curve))

    def __str__(self):
        #return '({}, {})'.format(self.x, self.y)
        return '('+str(self.x)+', '+str(self.y)+')'

    def getitem(self, index):
        return [self.x, self.y][index]

    def eq(self, Q):
        return (self.curve, self.x, self.y) == (Q.curve, Q.x, Q.y)

    def neg(self):
        return Point(self.curve, self.x, -self.y)


    def add(self, Q):
        """Add two points together.

        We need to take care of special cases:
         * Q is the infinity point (0)
         * P == Q
         * The line crossing P and Q is vertical.

        """
        assert self.curve == Q.curve

        # 0 + P = P
        if isinstance(Q, Inf):
            return self

        xp, yp, xq, yq = self.x, self.y, Q.x, Q.y
        m = None

        # P == Q
        if self == Q:
            if self.y == 0:
                R = Inf(self.curve)
            else:
                m = ((3 * xp * xp + self.curve.a) * self.mod_inverse(2 * yp, self.curve.p)) % self.curve.p

        # Vertical line
        elif xp == xq:
            R = Inf(self.curve)

        # Common case
        else:
            m = ((yq - yp) * self.mod_inverse(xq - xp, self.curve.p)) % self.curve.p

        if m is not None:
            xr = (m ** 2 - xp - xq) % self.curve.p
            yr = (m * (xp - xr) - yp) % self.curve.p
            R = Point(self.curve, xr, yr)

        return R

    def mul(self, n):
	
        if n == 0:
            return Inf(self.curve)
        if n == 1:
            return self;
        else:
            Q = self
            i = 1
            while i <= n-1:
                Q = Q.add(self);
                i+=1;
            return Q;


    def mod_inverse(self, a, n):
        """Return the inverse of a mod n.

        n must be prime.

        >>> mod_inverse(42, 2017)
        1969

        """
        b = n
        if abs(b) == 0:
            return (1, 0, a)

        x1, x2, y1, y2 = 0, 1, 1, 0
        while abs(b) > 0:
            q, r = divmod(a, b)
            x = x2 - q * x1
            y = y2 - q * y1
            a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

        return x2 % n

    def __rmul__(self, n):
        return self * n
		
                
class Inf(Point):
    """The custom infinity point."""
    def __init__(self, curve):
        self.curve = curve
        self.x = 0
        self.y = 0

    def eq(self, Q):
        return isinstance(Q, Inf)

    def neg(self):
        """-0 = 0"""
        return self

    def add(self, Q):
        """P + 0 = P"""
        return Q
    def __str__(self):
        #return '({}, {})'.format(self.x, self.y)
        return '('+str(self.x)+', '+str(self.y)+')'		
		