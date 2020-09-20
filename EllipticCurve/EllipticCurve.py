
import math
from Point import Inf 
from Point import Point 



class EllipticCurve(object):
    """Represents a single elliptic curve defined over a finite field."""
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.pointsGroup = self.findAllPoints();

    def eq(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

   
    def findOrder(self, point):
        order = 1; 
        result = point;

        while(not isinstance(result, Inf)):
            result = result.add(point);
            order += 1;
        return order;
	 
         
         
    def MaxOrder(self):
        max = 1; 
        for i in range(len(self.pointsGroup)):
            order = self.findOrder(self.pointsGroup[i]);   
            if(order>max):
                max = order;
        return max;
	
        
    def PmaxOrder(self):
        max = 1;
        maxP = self.pointsGroup[0];
        for i in range(len(self.pointsGroup)):
            order = self.findOrder(self.pointsGroup[i]);   
            if(order>max):
                max = order;
                maxP = self.pointsGroup[i];
        return maxP;
  
    def findAllPoints(self):
        pointsGroup = [];
        for x in range(0, self.p):
            
            roots = self.squareRoot(self.f(x));
            #roots is not None
            if (len(roots)==2):
                    pointsGroup.append(Point(self, x, math.floor(roots[0])));
                    #print (Point(self, x, roots[0]));
                    if (roots[0] != roots[1]):
                            pointsGroup.append(Point(self, x, math.floor(roots[1])));
                            #print (Point(self, x, roots[1]));
        #pointsGroup.append(Point(self, 0, 0));                    
        pointsGroup.append(Inf(self));
        
        return pointsGroup;
	
    def  f(self, x):
        return (pow(x,3,self.p) + math.fmod(self.a*x,self.p)+ self.b) % self.p;


    def squareRoot(self, y):
        #x = pow(y,math.floor((self.p + 1) / 4), self.p);
        x = pow(y,math.floor((self.p + 1) / 4)) % self.p;
        if ((x * x) % self.p == y):
            return [ x, (self.p - x) % self.p ];
        else:
            return [];

	# theoreme  Hasse 1939
    def bounds (self):
        sqrtp = math.floor(math.sqrt(self.p));
        bi = (self.p+1)-(2*sqrtp);
        bs = (self.p+1)+(2*sqrtp);
        return [bi,bs];

        

    def tostring(self):   
    
        ec = "E"+str(self.p)+" ("+str(self.a)+", "+str(self.b)+"): Y^2 = X^3 ";
            
        if(self.a>0):
            ec+="+"+str(self.a)+"X "; 
        else:
            if(a<0): 
                ec+=""+str(self.a)+"X "; 
        if(self.b>0):
            ec+="+"+str(self.b); 
        else:
            if(self.b<0):
                ec+=""+str(self.b);
            
        ec+= " mod "+str(self.p)+"\n";
            
        bounds = self.bounds();
        ec+= "curve borders:  "+str(bounds[0])+" <= Ep <= "+str(bounds[1])+"\n"+"EllipticCurve("+str(len(self.pointsGroup)-1)+"): "; 
        for items in self.pointsGroup:
            #if (not isinstance(items, Inf)):
            ec+=str(items);
        ec+="\n";
        return ec;
        #return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)
        
    
 