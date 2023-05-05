for num in range(1,501):
    print(num)
    prime=num%2==0
    print(prime)

    

#You can use unpacking with range like this:

for i in (1,10):
    print(*range(i,501,i))