#readlines() method
# f= open('myfile.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1= int(line.split(",")[0])   
#     m2= int(line.split(",")[1])   
#     m3= int(line.split(",")[2])   

#     print(f"marks of student {i} in maths is {m1}")
#     print(f"marks of student {i} in sst is {m2}")
#     print(f"marks of student {i} in eng is {m3}")
#     print(line)

#writelines() method
f=open("myfile.txt","w")
lines=['line 1','line 2','line 3']
for line in lines:
    f.write(line+"\n")
    print(line)



