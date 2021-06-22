from random import *


def main():
    getInputs()

def getInputs():
    noOfFlips = int(input("how many flips?\t"))
    simulateFlips(noOfFlips)

def simulateFlips(flipNumber):
    headCount = 0
    tailsCount = 0
    for i in range(flipNumber):
        if randint(1,2) == 1:
            headCount = headCount + 1
        else:
            tailsCount = tailsCount + 1
    
    displayResuts(flipNumber,headCount,tailsCount)
    

def displayResuts(flipTotal,headCount,tailsCount):
    headProportion = headCount/flipTotal
    tailsProportion = tailsCount/flipTotal
    
    print("Heads {0},   Tails {1}".format(headProportion,tailsProportion))
    
    
    
    
    
main()