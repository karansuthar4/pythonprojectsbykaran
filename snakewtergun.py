import random
def check(comp,user):
    if(comp==user):
        return 0
    
    if (comp==1 and user==0):
        return -1
    if (comp==1 and user==2):
        return -1
    if (comp==2 and user==0):
        return -1
    return 1
comp=random.randint(0,2)
user=int(input("0 for snake 1 for water 2 for gun:"))
score=check(comp,user)
print("user:" ,user)
print("computer:",comp)
if (score==0):
    print("draw")
elif(score==-1):
    print("computer win")
else:
    print("user win")