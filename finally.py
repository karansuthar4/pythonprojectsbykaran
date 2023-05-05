def func():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter the index number:"))
        print(l[i])
        return 1
              
    except:
        print("some errror occured:")
        return 0
    finally:
        print("i am always executed")
x=func()
print(x)