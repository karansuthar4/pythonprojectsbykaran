class employee:
    companyname="apple"
    
    def show(self):
        print(f"{self.name} is working in {self.companyname}.")
    @classmethod
    def showdetails(self,newcompanyname):
        self.companyname=newcompanyname
e1=employee()
e1.name='karan'
e1.show()
e1.showdetails('tesla')
e1.show()
print(employee.companyname)
