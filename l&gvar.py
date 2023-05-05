x=10 #global variable
def my_fun():
    global x #global keyword
    x=34
    y=11 #local variable
    print(y)
my_fun()
print(x)
