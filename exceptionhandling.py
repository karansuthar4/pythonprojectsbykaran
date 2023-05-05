"""try:
    num=int(input("enter an integer:>"))
except ValueError:
    print("num is not an int")"""

'''a=input("ENTER A NUM=>")
print(f"multiplication of num {a} is:")
try:
    for i in range(1,11):
        print(f"{int (a)}*{i}={(int (a)*i)}")
except:
    print("invalid syntax:")

print("some of imp lines")
print("end of program")'''

'''try:
    num=int(input("enter a num:"))
    a=[6,5]
    print(a[num])
except ValueError:
    print("num entered is not an int:")
except IndexError:
    print("invalid index:")'''
 
try:
    a=int(input("enter a value of a:"))
    b=int(input("enter a value of b:"))
    ans=a/b
    print("answer",ans)
except ValueError:
    print("entered value is not an int:")
except ZeroDivisionError:
    print("entered no is 0 which is not valid:")
except:
    print("error")






