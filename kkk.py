class Polygon:
  def __init__(self):
    pass
  def set(self):
    pass
  def numOfSides(self):
    return self.__num

class Pentagon(Polygon):
  def __init__(self, **kwargs):
    self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
  def set(self, st=""):
    self.__num=st
  def numOfSides(self):
    return self.__num
  
class Octagon(Polygon):
  def __init__(self, **kwargs):
    self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
  def set(self, st=""):
    self.__num=st
  def numOfSides(self):
    return self.__num

class Triangle(Polygon):
  def __init__(self, **kwargs):
    self.__num = int(kwargs["keys"]) if "keys" in kwargs.keys() else 0
  def set(self, st=""):
    self.__num=st
  def numOfSides(self):
    return self.__num

pentagon=Pentagon()
octagon=Octagon()
triangle=Triangle()
triangle.set(3)
pentagon.set(5)
octagon.set(8)
print(triangle.numOfSides())
print(pentagon.numOfSides())
print(octagon.numOfSides())
