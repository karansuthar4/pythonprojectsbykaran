class person:
    name="karan"
    occupation="data scientist"
    networth=500000
    def info(self):
        
        print(f"{self.name} is a {self.occupation} and his net worth is:{self.networth}")


a=person()
b=person()
c=person()

a.name="jagdish"
a.occupation="web developer"

b.name="uttam"
b.occupation="app developer"

a.info()
b.info()
c.info()