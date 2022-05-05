class MCU:
  def __init__(self,name="", born=0, weapons=[],bestActorName=""):
    self.__name = name
    self.__born = born
    self.__weapons = weapons
    self.__bestactorname = bestActorName
  def setname(self,name=""):
    self.__name=name
  def setborn(self,born=0):
    self.__born=born
  def setbestactorname(self,bestactorname=""):
    self.__bestactorname=bestactorname
  def getName(self,name=""):
    return self.__name
  def getborn(self,born=0):
    return self.__born
  def getbestactorname(self):
    return self.__bestactorname
  def addweapon(self, weapon=""):
    self.__weapons = weapon
  def removeweapon(self):
    del self.__weapons
  def getweapon(self):
    return self.__weapons

obj = MCU()
print(obj)
obj.setname("Tom Holland")
obj.setborn(1996)
obj.addweapon("superpower")
obj.setbestactorname("Chris Hemsworth")
print("name",obj.getName())
print("born",obj.getborn())
print("weapons",obj.getweapon())
print("bestActorName",obj.getbestactorname())
