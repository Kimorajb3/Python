class Employee():

    def __init__(self,name,ID,dept,JT):
        self.name=name
        self.id=ID
        self.department=dept
        self.jt=JT


    def setname(self,name):
        self.name=name
    def setID(self,ID):
        self.id=ID
    def setdept(self,dept):
        self.department=dept
    def setJT(self,JT):
        self.jt = JT

    def __str__(self):
        return "Name: %s, ID: %s, Department: %s, Job Title: %s"%(self.name,self.id,self.department,self.jt)
