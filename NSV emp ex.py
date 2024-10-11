class emp:
    company="Infosys"
    def getdetails(self):
        self.ename=input("Enter the name:")
        self.eid=int(input("Enter the eid:"))
        self.esal=int(input("Enter the esal:"))
        self.design=input("Enter the edesign:")
        print(self)
    def putdetails(self):
        print("Ename=",self.ename)
        print("Eid=",self.eid)
        print("Esal=",self.esal)
        print("edesign=",self.design)
        print("Company=",emp.company)
        print(self)
e1=emp()
print(e1)
e1.getdetails()
e1.putdetails()
e2=emp()
e2.getdetails()
e2.putdetails()

print(e1.ename)
print(e2.ename)



