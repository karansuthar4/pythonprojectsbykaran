
a= input("write a number between 5 and 9: ")

if(a == "quit"):
    pass
elif(int(a) <5 or int(a) >9):
    raise ValueError("your input is not between 5 and 9.")