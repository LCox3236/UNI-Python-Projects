import os
from graphics import *
import random

def personalGreeting():
    name = input("whats your name?\n")
    print ("Hello", name, ", how are you?")
    
#-------------------------------------------------------------------------------

def formalName():
    firstName = input("whats your first name?\n")
    familyName = input("whats your family/ last name?\n")
    print (firstName[0].upper(),".",familyName)
    
#-------------------------------------------------------------------------------

def kilos2pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print(round(kilos,2),"Kilos in pounds is", round(pounds,2))
    
#-------------------------------------------------------------------------------

def generataEmail():
    fName = input("whats your first name?\n")
    sName = input("whats your surname?\n")
    year = input("what year did you start university?\n")
    print(sName[:3]+"."+fName[0]+"."+year[2:]+"@myport.ac.uk")
    
#-------------------------------------------------------------------------------
    
def gradeTest():
    grades = "AAABBCCFFFF"
    points = int(input("how many points did you get?\n"))
    print (grades[-points])
    
#-------------------------------------------------------------------------------

def graphicLetters():
    win = GraphWin("graphicLetters",500,500)
    word = input("please enter a word\n")
    for i in range (len(word)):
        p = win.getMouse()
        message = Text((p), word[i])
       # size = random.randint(0,20)
       # message.setSize(size)
        message.setSize(20)
        message.draw(win)
    
#-------------------------------------------------------------------------------

def singAsong():
    word = input("whats the word\n")
    lines = int(input("how many lines?\n"))
    wordsALine = []
    for i in range (lines):
        count = int(input("how many words on line {}\n".format(i+1)))
        wordsALine.append(count)
   # print (wordsALine)
    for i in range (len(wordsALine)):
        print (word*wordsALine[i])
    
#-------------------------------------------------------------------------------

def exchageTable():
    euros =0 
    pounds = 0
    for i in range (10):
        euros = euros +10
        pounds = euros/1.09
        print("{0:5.2f} euros is equal to {1:5.2f} Pounds".format(euros,pounds))
       
 #-------------------------------------------------------------------------------       

def makeAcronym():
    phrase = input("enter a phrase\n")
    wordsInPhrase = phrase.split()
    acronym = ""
    for i in range (len(wordsInPhrase)):
        word = wordsInPhrase[i]
        acronym = acronym+(word[0])
    print (acronym.upper())
        
#-------------------------------------------------------------------------------

def nameToNumber():
    name = input("whats your name?\n").lower()
    total = 0
    for i in range (len(name)):
        number = abs(97 - ord(name[i]))+1
        total = total + number
        print(number)
    print (total)
        
#-------------------------------------------------------------------------------

def fileInCaps():
    file = open("Prac04TXT.txt", "r")
    for line in file:
        print(line.upper())

#-------------------------------------------------------------------------------








        