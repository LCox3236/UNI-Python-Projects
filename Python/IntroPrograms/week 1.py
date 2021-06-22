def sayname():
    name = input("whats your name?")
    print (name)
    
#-----------------------------------------------------------------------------------------------------------------------------------
   
def sayhello2():
    print ("hello")
    print ("world")

#-----------------------------------------------------------------------------------------------------------------------------------

def euros2pounds():
    euro = float(input("Please enter a value in euros\n"))
    if euro < 0 :
        print ("this is not a valid value")
    else:
        print (euro / 1.12)
    
#-----------------------------------------------------------------------------------------------------------------------------------

def addup():
    num1 = int(input("please enter the first number\n"))
    num2 = int(input("please enter the second number\n"))
    print (num1 + num2)
    
#---------------------------------------------------------------------------------------------------------------------------------
 
def ChangeCounter():
    OneP = int(input("How many 1p coins do you have?\n"))
    TwoP = int(input("How many 2p coins do you have?\n"))
    FiveP = int(input("How many 5p coins do you have?\n"))
    total = OneP + (TwoP * 2) + (FiveP * 5)
    print("£" and total)
    
#-----------------------------------------------------------------------------------------------------------------------------------

def tenhellos():
    for i in range(10):
        print("hello")
    
#-----------------------------------------------------------------------------------------------------------------------------------
    
def counttoten():
    for i in range(10):
        print(i+1)
    
#-----------------------------------------------------------------------------------------------------------------------------------

def weighttables():
    kilo=0
    pound=0
    print ("Kilograms ------ Pounds")
    for i in range(11):
        
        
         print(kilo,  "--------------",  pound)
         kilo = kilo + 10
         pound = kilo * 2.2
    
#-----------------------------------------------------------------------------------------------------------------------------------
    
def futurevalue():
   # total = 0
    interst = 0.055
    
    inital = int(input("What is the inital ammount of money?\n"))
    
    years = int(input("How many years will the investment last?\n"))
    
   # total = inital
    
    for i in range (years):
        inital = inital + (inital * interst)
        print ("year ", i+1, " = ", inital)
        
    print ("\n\nTotal = ", inital)
   