from math import *

class CircleInfo:
    def __init__(self, r):
        self.radius = r
    def calculateArea(self):
        return self.radius**2*pi
    def calculateCircumfrence(self):
        return 2*pi*self.radius
    def circleInfo(self):
        print ("area = ", self.calculateArea(),"     circumfrence = ",self.calculateCircumfrence())
        