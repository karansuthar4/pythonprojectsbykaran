class Surname:
    surname='suthar'
    def name(self,surname):
        print(self.surname)
class Son:
    Sonname="karan"
    def son(self,Sonname):
        print(self.Sonname)
class Father:
    fathername="vijaybhai"
    def father(self,fathername):
        print(self.fathername)
class Mother:
    mothername="geeetaben"
    def mother(self,mothername):
        print(self.mothername)
class full(Surname,Son,Father,Mother):
    def fullname(self):
        print(f"{self.surname} {self.Sonname} {self.fathername}")
        print(f"{self.surname} {self.Sonname} {self.mothername}")
s1=full()
s1.fullname()