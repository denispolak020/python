import os
import math

clear = lambda: os.system('cls')

class Bod:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self,x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self,y):
        self.y = y
    
    def gety(self):
        return self.y

    def nastavSouradnice(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"
    
class Usecka:

    def __init__(self, A: Bod, B: Bod):
        self.__a = A
        self.__b = B
    
    def geta(self):
        return self.__a

    def seta(self,a : dict):
        self.__a = a

    def getb(self):
        return self.__b

    def setb(self,b : dict):
        self.__b = b


    def nastavSouradnice(self, u, v, x, y):
        self.__a.nastavSouradnice(u, v)
        self.__b.nastavSouradnice(x, y)

    def __str__(self):
        return  f"[{self.__a.x},{self.__a.y}][{self.__b.x},{self.__b.y}]"

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.x - self.__b.x, 2) + math.pow(self.__a.y - self.__b.y, 2))
    
clear()

B = Bod()
B.nastavSouradnice(1, -2)
print(B)

D = Bod(1, 3)
E = Bod(4, -1)
U = Usecka(D, E)

B.setx(3)
print(B.getx())
B.sety(-1)
print(B.gety())

U.seta(1)
print(U.geta())
U.setb(4)
print(U.getb())

print(U)
print(f"{U.delkaUsecky():.2f}")
