def  checkarm(num):
    r=0
    sum=0
    while(num>0):
        r=num%10
        sum=sum+r**3
        num=num//10
    return sum

for n in range(1,500):
    print(n)
    temp= checkarm(n)
    if(temp==n):
        print("n is armstrong no.")
    else:
        print("n is not armstrong no.")