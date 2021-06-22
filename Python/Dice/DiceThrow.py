import random

class Dice:
    def __init__(self):
        self.sideNums = [1,2,3,4,5,6]
        
    def diceThrow(self):
            return self.sideNums[random.randint(0,5)]
        
        