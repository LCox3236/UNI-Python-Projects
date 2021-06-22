# Practical Worksheet 3: Graphical Programming
# your name, your number

from graphics import *
from math import *
def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(80, 90),Point(120,90))
    arms.draw(win)
    leg1 = Line(Point(100,120),Point(115,135))
    leg1.draw(win)
    leg2 = Line(Point(100,120),Point(85,135))
    leg2.draw(win)

#-------------------------------------------------------------------------------

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")

#-------------------------------------------------------------------------------

def drawcircle():
    win = GraphWin("Circle drawer")
    radius = int(input("enter the radius\n"))
    C = Circle(Point(100,100), radius)
    C.draw(win)
    
#-------------------------------------------------------------------------------

def DrawArcheryTarget():
    win = GraphWin("Target drawer")
    
    blue = Circle(Point(100,100),75)
    blue.setFill("Blue")
    blue.draw(win)
    
    red = Circle(Point(100,100),50)
    red.setFill("Red")
    red.draw(win)
    
    yellow = Circle(Point(100,100),25)
    yellow.setFill("Yellow")
    yellow.draw(win)
    
#-------------------------------------------------------------------------------

def DrawRectangle():
    win = GraphWin("Rectangle drawer")
    width = int(input("enter Width\n"))
    height = int(input("enter Height\n"))
    
    leftmostpoint = (200-width)//2
    rightmostpoint = leftmostpoint + width
    
    topmostpoint = (200-height)//2
    bottommostpoint = topmostpoint + height
    
    rect = Rectangle(Point(leftmostpoint,topmostpoint),Point(rightmostpoint,bottommostpoint))
    rect.draw(win)  
    
#-------------------------------------------------------------------------------
    
def BlueCircle():
    win = GraphWin("Blue Circle drawer",500,500)
    for i in range(10):
        centre = win.getMouse()
        blue = Circle(centre,50)
        blue.setFill("Blue")
        blue.draw(win)
    win.close()
    
#-------------------------------------------------------------------------------
    
def TenLines():
    win = GraphWin("Line drawer",600,600)
    for i in range(10):
        message = Text(Point(100,100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

#-------------------------------------------------------------------------------

def TenColouredRectangles():
    win = GraphWin("Coloured Rectangles",600,600)
    message = Text(Point(250,25),"Enter Colour then click twice for rectangle")
    message.setSize(15)
    message.draw(win) 
    colourInput = Entry(Point(250,50),50)
    colourInput.draw(win)
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rectangle = Rectangle(p1,p2)
        rectangle.setFill(colourInput.getText())
        rectangle.draw(win)

#-------------------------------------------------------------------------------

def FiveClickStickFigure():
    win = GraphWin("Five Click Stick Figure", 700,700)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    p4 = win.getMouse()
    p5 = win.getMouse()
    headRadius = sqrt(((p2.getY() - p1.getY())**2) + ((p2.getX() - p1.getX())**2))
    head = Circle(p1,headRadius)
    head.draw(win)








    
