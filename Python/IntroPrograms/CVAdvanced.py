class CVAdvanced:
    def __init__(self, name, initialSkill):
        self.studentName = name
        self.skills = []
        self.skills.append(initialSkill)
        
    def addSkill(self, newSkill):
        self.skills.append(newSkill)
    
    def removeSkill(self, rmskill):
        if rmskill in self.skills:
            self.skills.remove(rmskill)
        
    def info(self):
        return "student: {0}\nskills {1}: ".format(self.studentName, self.skills)
        # for i in self.skills:
        #     return self.skills[i]
 