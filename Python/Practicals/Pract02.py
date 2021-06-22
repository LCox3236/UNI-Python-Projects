import math

def CircumferenceOfCircle():
    radius = float(input("Please enter the radius of the circle\n"))
    circumference = 2*radius*math.pi
    print(circumference)
    
#-------------------------------------------------------------------------------

def AreaOfCircle():
    Radius = float(input("Please enter the radius of the circle\n"))
    Area = math.pi * Radius**2
    print(Area)    

#-------------------------------------------------------------------------------

def CostOfPizza():
    Diameter = float(input("Please enter the Diameter of the Pizza\n"))
    Area = math.pi * ((Diameter/2)**2)
    Cost = Area * 1.5
    print(Cost)

#-------------------------------------------------------------------------------

def SlopeOfLine():
    X1 = int(input("Please enter the X value of the first point\n"))
    Y1 = int(input("Please enter the Y value of the first point\n"))
    X2 = int(input("Please enter the X value of the Second point\n"))
    Y2 = int(input("Please enter the Y value of the Second point\n"))
    slope = (Y2 - Y1) / (X2 - X1)
    print(slope)

#-------------------------------------------------------------------------------

def DistanceBetweenPoints():
    X1 = int(input("Please enter the X value of the first point\n"))
    Y1 = int(input("Please enter the Y value of the first point\n"))
    X2 = int(input("Please enter the X value of the Second point\n"))
    Y2 = int(input("Please enter the Y value of the Second point\n"))
    distance = math.sqrt( ( (X2 -X1)**2 ) + ( (Y2 - Y1)**2 ) )
    print(distance)

#-------------------------------------------------------------------------------

def TravelStatistics():
    Speed = float(input("Enter the average speed, in km/h:\n"))
    duration = float(input("Enter the duration of travel in hours:\n"))
    distance = Speed * duration
    fuelUsed = distance / 5
    print("The distance traveled is ", distance, " km")
    print("the ammount of fuel used was ", fuelUsed, " litres")
    
#-------------------------------------------------------------------------------

def SumOfNumbers():
    x = 0
    loop = int(input("Enter which number to add all up to?\n"))
    for i in range (loop+1):
        x = x + i
    print("the total of all numbers up to and including", loop, " = ", x)
    
#-------------------------------------------------------------------------------

def AverageOfNumbers():
    total = 0
    ListOfNumbers = []
    loop = int(input("how many numbers do you want to enter?\n"))
    for i in range(loop):
        num = int(input("Please enter a number\n"))
        ListOfNumbers.append(num)
    for x in ListOfNumbers:
        total = total + x
    average = total / loop
    print("The average of the numbers you entered is ",average)

#-------------------------------------------------------------------------------

def SelectCoins():
    total = int(input("Please enter a value in pence\n"))
    TwoPound = total//200
    remainder = total%200

    OnePound = remainder//100
    remainder = remainder%100
    
    FiftyP = remainder//50
    remainder = remainder%50
    
    TwentyP = remainder//20
    remainder = remainder%20

    TenP = remainder//10
    remainder = remainder%10

    FiveP = remainder//5
    remainder = remainder%5

    TwoP = remainder//2
    remainder = remainder%2

    OneP = remainder//1
    remainder = remainder%1

    print("£2  = ", TwoPound, "\n£1  = ",OnePound, "\n50p = ", FiftyP, "\n20p = ", TwentyP, "\n10p = ", TenP, "\n5p  = ", FiveP, "\n2p  = ", TwoP, "\n1p  = ", OneP)








