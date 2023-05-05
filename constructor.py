#default argumment:
class person:
    def __init__(self):
        print("karan is data scientist")
    
a=person()

#parameterized argument:
class person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
        print(f"{self.name} is a {self.occ}.")
a=person("karan","data scientist" )
b=person("kiran","data analyst")
    