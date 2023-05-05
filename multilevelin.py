class grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class father(grandfather):
    def __init__(self,grandfathername,fathername):
        self.fathername=fathername
        grandfather.__init__(self,grandfathername)
class son(father):
    def __init__(self,grandfathername,fathername,sonname):
        self.sonname=sonname
        father.__init__(self,grandfathername,fathername)
    def printname(self):
        print('grandfathername:',self.grandfathername)
        print('fathername:',self.fathername)
        print('sonname:',self.sonname)
s1=son('dhanjibhaii','vijaybhai','karan')
s1.printname()
        