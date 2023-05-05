def  checkarm(num):
    r=0
    sum=0
    while(num>0):
        r=num%10
        sum=sum+r**3
        num=num//10
    return sum

n=int(input("enter value of n"))
temp= checkarm(n)
if(temp==n):
    print("n is armstrong no.")
else:
    print("n is not armstrong no.")