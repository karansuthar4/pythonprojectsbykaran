class library:
    def __init__(self,name,aname):
        self.name=name
        self.aname=aname
    @classmethod
    def forstr(cls,str):
        return cls(str.split("_")[0],str.split("_")[1])
    
str="harry_karan"
e1=library.forstr(str)
print(e1.name,e1.aname)
