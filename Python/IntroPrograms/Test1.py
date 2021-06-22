 import math
 def PepperoniPizza():
     base = int(input("enter raidius of pizza base in cm\n"))
     cheese = int(input("enter the radius of the cheese on the pizza in cm\n"))
     crustwidth = base - cheese
     print ("\n1 - The width of the pizzas crust is ",crustwidth,"cm\n")
     
     cheesearea = math.pi*(cheese**2)
     print ("2 - the area of the cheese region is ", cheesearea, "cm^2\n")
     
     basearea = math.pi*(base**2)
     
     crustarea = basearea - cheesearea
     print("3 - the area of the crust region is ", crustarea, "cm^2\n")
     
     pepperonipeices = int(cheesearea // 30)
     print("4 - the number of peices of pepperoni added is", pepperonipeices)