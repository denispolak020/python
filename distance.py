from math import sin, cos, sqrt, atan2, radians

R = 6373.0
class distance:
    def __init__(self):
            
        self.lat1 = radians(50.902434)
        self.lon1 = radians(14.633316)
        self.lat2 = radians(50.765616)
        self.lon2 = radians(15.049353)

        self.dlon = self.lon2 - self.lon1
        self.dlat = self.lat2 - self.lat1
    def vzorecek(self):
        a = sin(self.dlat / 2)**2 + cos(self.lat1) * cos(self.lat2) * sin(self.dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        print(distance,"km")
d=distance()
d.vzorecek()
