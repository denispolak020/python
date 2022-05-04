class Vehicle:
    def __init__(self,light,door):
        self.light = light
        self.door = door
    def __str__(self):
        return f"The vehicle has {self.light} and {self.door}."


class Car(Vehicle):    
    def __init__(self, light, door):
        super().__init__(light, door)
    def __str__(self):
        return f"The car has {self.light} and {self.door}."
    
    def Ride(self, ride):
        self.ride = ride
        print(f"The car is driving{self.ride}.")


class Motorcycle(Vehicle):
    def __init__(self, wheels, mirrors):
      self.mirrors = mirrors
      self.wheels = wheels
      super().__init__(wheels, mirrors)
    def __str__(self):
        return f"The motorcycle has {self.mirrors} and {self.wheels}."
    def Speed(self, speed):
      self.speed = speed
      print(f"The motorcycle is going {self.speed}.")

class Truck(Vehicle):
    def __init__(self, exhaust, seats):
      self.exhaust = exhaust
      self.seats = seats
      super().__init__(exhaust, seats)
    def __str__(self):
      return f"The truck has 2 {self.exhaust} and 3 {self.seats}."

    def Fuel(self, fuel):
      self.fuel = fuel
      
      

    

vehicle=Vehicle("lights","doors") 
print(vehicle)


motorcycle=Motorcycle("wheels","mirrors")
print(motorcycle)
motorcycle.Speed("90KM/H")

truck=Truck("exhaust","seats")
print(truck)
truck.Fuel("50L")

car=Car("lights","doors")
print(car)
