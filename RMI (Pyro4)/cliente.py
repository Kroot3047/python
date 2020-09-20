import  Pyro4
import os


ns = Pyro4.locateNS()
uri = ns.lookup('simpleObjectCalculator')
calculator = Pyro4.Proxy(uri)

a = input("a : ")
b = input("b : ")
c = calculator.add(a, b)
print("a + b = ",c)

os.system("pause")