class CVBasic:
    def __init__(self, name, initialSkill):
        self.studentName = name
        self.skill = initialSkill
        
    def addSkill(self, newSkill):
        if self.skill == "":
            self.skill = newSkill
    
    def removeSkill(self):
        self.skill = ""
        
    def info(self):
        return "student: {0}\nskill: {1}".format(self.studentName, self.skill)
        
    
    