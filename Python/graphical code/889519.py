from graphics import *


def drawPatchNine(win, colour, startX, startY):
   
    endX=startX+100
    endY=startY+100
    
    colour1 = colour
    colour2 = "white"
    
    for i in range (10):
        rectangle = Rectangle(Point(startX,startY),Point(endX, endY))
        rectangle.setFill(colour2)
        rectangle.setOutline(colour2)
        rectangle.draw(win)
        endX = endX - 10
        endY = endY - 10
        
        colour1,colour2 = colour2,colour1
        
       

def drawPatchOne(win, colour, startX, startY):

    colour1 = colour
    colour2 = "white"
    
    for i in range (4):        
        for x in range (2):
            
            rectangle = Rectangle(Point(startX,startY),Point(startX+50,startY+25))
            rectangle.setFill(colour2)
            rectangle.setOutline("black")
            rectangle.draw(win)
            
            divider = Line(Point(startX+25,startY),Point(startX+25,startY+25))
            divider.draw(win)
        
            rect1 = Rectangle(Point(startX+5,startY+0),Point(startX+20,startY+10.5))
            rect1.setFill(colour1)
            rect1.draw(win)
            
            rect2 = Rectangle(Point(startX+5,startY+14.5),Point(startX+20,startY+25))
            rect2.setFill(colour1)
            rect2.draw(win)
            
            rect3 = Rectangle(Point(startX+25,startY+5),Point(startX+35,startY+20))
            rect3.setFill(colour1)
            rect3.draw(win)
            
            rect4 = Rectangle(Point(startX+40,startY+5),Point(startX+50,startY+20))
            rect4.setFill(colour1)
            rect4.draw(win)
        
            startX = startX + 50
            colour1,colour2 = colour2,colour1
            
        startY = startY + 25
        startX = startX - 100
       
        colour1,colour2 = colour2,colour1
    
    


def mainFull():
    
    gridSize, colours = getInputs() 
    
    patchworkSize = gridSize * 100
    patchNineBorder = patchworkSize - 200
    
    win = GraphWin("draw Patch", patchworkSize, patchworkSize)
    win.setCoords(0,0,patchworkSize,patchworkSize)
    
    startX = 0
    startY = 0
      
    
    for i in range (gridSize):
        for q in range (gridSize):
            
            if startX < patchNineBorder and startY < patchNineBorder:
                if startX == startY:
                    drawPatchNine(win, colours[1], startX, startY)
                    
                elif startX > startY:
                     drawPatchNine(win, colours[2], startX, startY)
                
                else:
                    drawPatchNine(win, colours[0], startX, startY)

            else:
                if startX == startY:
                    drawPatchOne(win, colours[1], startX, startY)
                    
                elif startX > startY:
                     drawPatchOne(win, colours[2], startX, startY)
                     
                else:
                    drawPatchOne(win, colours[0], startX, startY)

            startX = startX + 100
            
        
        startX = startX - patchworkSize
        startY = startY + 100
        
    
    while True:
        click = win.getMouse()
        clickedX = click.getX()
        clickedY = click.getY()
        bottomLeft = Point(clickedX-(clickedX%100),clickedY-(clickedY%100))  
        topRight = Point(clickedX+(100-clickedX%100),clickedY+(100-clickedY%100))  
        box = Rectangle(bottomLeft,topRight)
        box.setWidth(5) 
        box.draw(win)
        editingGrid(win, bottomLeft,topRight, box)
    
    
def getInputs():
    
    validGridSizes = [5,7,9]
    sizeSet = False
    while not sizeSet:
        gridSize = int(input("enter the grid size\t"))
        if gridSize not in validGridSizes:
            print("the only valid sizes are 5, 7, and 9")
        else:
            sizeSet = True    
        
    
    colours = ["first","second","third"]
    replaced = 0
    while replaced < 3:
        colour = input("Enter the {} colour,\t".format(colours[replaced]))
        if colour == "red" or colour == "green" or colour == "blue" or colour == "magenta" or colour == "orange" or colour == "pink":
            colours[replaced] = colour
            replaced = replaced + 1 
        else:
            print("this is not a valid colour.\n")
    return(gridSize, colours)



def editingGrid(win, bottomLeft,topRight, box):
    enterPressed = False
    dPressed = False
    
    while not enterPressed:
        
        keyPress = win.getKey()
        
        if keyPress == "d":
            erase = Rectangle(bottomLeft,topRight)
            erase.setFill("white")
            erase.setWidth(0)
            erase.draw(win)
            
            dPressed = True

        if keyPress == "m":
            if dPressed == True:
                    drawPatchNine(win,"magenta",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False



        if keyPress == "g":
            if dPressed == True:
                    drawPatchNine(win,"green",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False

        if keyPress == "b":
            if dPressed == True:
                    drawPatchNine(win,"blue",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False

        if keyPress == "r":
            if dPressed ==True:
                    drawPatchNine(win,"red",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False


        if keyPress == "o":
            if dPressed == True:
                    drawPatchNine(win,"orange",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False


        if keyPress == "p":
            if dPressed == True:
                    drawPatchNine(win,"pink",bottomLeft.getX(),bottomLeft.getY())
                    dPressed = False


        box.undraw()
        box.draw(win)
       
        if keyPress == "Return":
            enterPressed = True
            box.undraw()
    
    
        if keyPress == "Escape":
            enterPressed = True
            win.close()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    