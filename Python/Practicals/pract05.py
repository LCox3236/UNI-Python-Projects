#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import math

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2
    
def circumferenceOfCircle(radius):
    return 2 * math.pi * radius    
    
def circleInfo():
    radius = int(input("please enter the radius\n"))
    print(areaOfCircle(radius))
    print(circumferenceOfCircle(radius))

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    window = GraphWin()
    drawCircle(window,Point(100,100),50,"white")
    drawCircle(window,Point(100,100),25,"brown")
    drawCircle(window,Point(100,100),10,"black")
    
# For exercise 5
def drawBrownEye(win, centre, radius):
    pass
    # Remove pass and add your code here
    
