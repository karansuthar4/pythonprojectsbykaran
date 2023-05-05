from functools import reduce
l=[1,2,4,5,6]
newl=reduce(lambda x,y:x+y,l)
print(newl )
