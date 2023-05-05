# double=lambda x:x*2
# cube=lambda x:x*x*x
# mul=lambda x,y:x*y
# avg=lambda x,y,z:x+y+z/3
# print(double(4))
# print(cube(9))
# print(mul(5,4))
# print(avg(4,8,2))

def appl(fx,value):
    return 6+fx(value)
print(appl(lambda x:x*x,3))
