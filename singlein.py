class employee:
    def __init__(self, id , name):
        self.id= id
        self.name=name
    def Details(self):
        print(f"The name of employee:{self. id} iis {self.name}")
class programmer(employee):
    def language(self):
        print('the default language is python')
e1=employee(101,'harry')
e1.Details()
e2=programmer(102,'karan')
e2.Details()
e2.language()