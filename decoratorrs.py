def greet(fx):
    def mfx(*args,**kwrgs):
        print("good morning")
        fx(*args,**kwrgs)
        print("thank you for using this function")
    return mfx
@greet
def hello():
    print("hello! i am karan suthar")

hello()

@greet
def sum(a,b):

    print(a+b)  

sum(2,6)