#reading the file:
f=open('myfile.txt','r')
contents=f.read()
print(contents)
f.close()
#writing in the file:
f=open('myfile2.txt','w')
f.write("good perfomance virat kohli")
f.close()
#appending the file:
f=open('myfile.txt','a')
f.write('i am studyinng in imscit')
f.close()
#with statement:
with open('myfile.txt','r')as f:
    f.read()