
class Lecturer:
    def __init__(self, Fname, Lname, salary):
        self.firstName = Fname
        self.lastName = Lname
        self.salary = salary
        self.Units = []
        
    def addUnit(self, unitName):
        self.units.append(unitName)
        
    
    def removeUnit(self, UnitName):
        if unitName in units:
            units.remove("unitName")
        else:
            print("this unit does not exist")
                       
    def wageRise(self, percentageIncrease):
        self.salary = self.salary*percentageIncrease%
        
    def lecturerInfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.salary)
        print(self.Units)