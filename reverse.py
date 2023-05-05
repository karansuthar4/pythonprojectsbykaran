no=379
rev=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("rev no=",rev)