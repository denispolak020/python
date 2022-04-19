class Leapyear():

    def __init__(self):

        self.year = int(input("vloz rok:")) 

    def Leapyear1(self):

        if (self.year%400==0) or (self.year%4==0 and self.year%100!=0):#výpočet

            print("LEAP YEAR")

        else:

            print ("NOT LEAP YEAR")

        print(self.year)