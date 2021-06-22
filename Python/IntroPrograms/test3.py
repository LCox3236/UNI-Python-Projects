from graphics import *

def circles():
    win = GraphWin("Circles",600,600)
    for i in range(9):
        clickPoint = win.getMouse()
        if clickPoint.getX() > 400:
            colour = "blue"
        elif clickPoint.getX() > 200:
            colour = "white"
        else:
            colour = "red"
        circle = Circle((clickPoint),30)
        circle.setFill(colour)
        circle.draw(win)
        
        
def circles2():
    win = GraphWin("Circles2",600,600)
    startPoint = Point(30,150)
    for i in range(30):
        clickPoint = win.getMouse() 
        if clickPoint.getX() > 400:
            colour = "blue"
        elif clickPoint.getX() > 200:
            colour = "white"
        else:
            colour = "red"
        circle = Circle(startPoint,30)
        circle.setFill(colour)
        circle.draw(win)
        startPoint.move(60,0)
        if (startPoint.getX() + 30) > 600:
            startPoint.move(-600,-60)
    click = win.getMouse()
    win.close()
    
    