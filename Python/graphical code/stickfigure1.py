from graphics import *

def footballPlayer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(80, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(120, 170))
    leg2.draw(win)
  
    ground = Line(Point(0,170),Point(300,170))
    ground.draw(win)
    
    football = Circle(Point(145,160),10)
    football.setFill("red")
    football.draw(win)

    goalPost = Rectangle(Point(240,170),Point(250,40))
    goalPost.setFill("blue")
    goalPost.draw(win)
    
    goalText = Text(Point(150,15),"")
    goalText.setSize(20)
    goalText.draw(win)
    message = ("GOAL!!!!")
    
    for i in range (8):
        moveBall = win.getMouse()
        football.move(15,0)
        goalText.setText(message[:i+1])
        
        
       
        
        