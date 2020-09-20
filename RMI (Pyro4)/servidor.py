import Pyro4
import os

#os.system("python -m Pyro4.naming &")


@Pyro4.expose
class Calculator:
    def add(self, a, b):
    	print("calculing "+a+" + "+b+" ...." )
    	return  int(a) + int(b)





daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)
ns = Pyro4.locateNS()
ns.register('simpleObjectCalculator', uri)
print("server is ready ! on URI : \n",uri)
daemon.requestLoop()
