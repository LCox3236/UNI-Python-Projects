#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *

def main():
    doorColour, lightsOn, windowSize, houseNumber = getInputs()
    drawHouse(doorColour, lightsOn, windowSize, houseNumber)

def getInputs():
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    windowSize = int(input("enter the size of the display window.\t"))
    houseNumber = int(input("enter the house number\t"))
    return doorColour, lightsOn, windowSize, houseNumber

def drawHouse(doorColour, lightsOn, windowSize, houseNumber):
    win = GraphWin("House", windowSize, windowSize)
    win.setCoords(0,0,windowSize,windowSize)
    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198,60))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)
    
def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

main()
