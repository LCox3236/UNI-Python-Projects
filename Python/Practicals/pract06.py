#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------
from math import *
from graphics import *

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    win = GraphWin("Draw Coloured Eye", 600,500)
    
    #drawCircle(win,centre,radius,colour)
    
    
#-------------------------------------------------------------------------------


def fastFoodOrderPrice():
    price = int(input("Enter the order price\t"))
    if price < 10:
        price = price + 1.15
    print ("The total price of your order is ",price)
    
#-------------------------------------------------------------------------------

def whatToDoToday():
    temperature = int(input("What is the temperture today?\t"))
    if temperature > 25:
        print("swim in the sea")
    elif temperature >= 10 and temperature <= 25:
        print ("shopping in Gunwharf Quays")
    elif temperature < 10:
        print ("watch a film at home")
        
#-------------------------------------------------------------------------------

def displaySquareRoots(start,end):
    while start <= end:
    
        print("the squre root of",start,"is {0:1.3f}".format(sqrt(start)))
        start = start +1
        
#-------------------------------------------------------------------------------

def calculateGrade(mark):
    if mark > 20 or mark < 0:
        print("this is an invalid score")
    elif mark >= 16 and mark <= 20:
        print ("This is a Grade A")
    elif mark >= 12 and mark <= 15:
        print("This is a Grade B")
    elif mark >= 8 and mark <= 11:
        print("This is a Grade C")
    elif mark <= 7:
        print("This is a Grade F")
    
#-------------------------------------------------------------------------------

def peasInAPod():
    noOfPeas = int(input("how many peas?\t"))
    ScreenXValue = noOfPeas*100
    win = GraphWin("Peas In A Pod",(ScreenXValue),100)
    circleX = 50
    for i in range(noOfPeas):
        pea = Circle(Point(circleX,50),49)
        circleX = circleX+100
        pea.setFill("green")
        pea.draw(win)
        
#-------------------------------------------------------------------------------

def ticketPrice(distance,passengerAge):
    totalPrice = (((distance*15)/100)+3)
    if passengerAge >= 60 or passengerAge <= 15:
        totalPrice = totalPrice * 0.60
    print (totalPrice)

#-------------------------------------------------------------------------------




def drawPatchWindow():
    win = GraphWin()
    rectangle = Rectangle(Point(0,10),Point(90,100))
    rectangle.setFill("red")
    rectangle.setOutline("red")
    rectangle.draw(win)
        












































