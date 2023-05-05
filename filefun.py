# seek() function

# with open('myfile.txt','r') as f:
#     f.seek(9)
#     data=f.read(5)
#     print(data)

# tell() function:

# with open('myfile.txt','r') as f:
#     data=f.read(9)
#     curposition=f.tell()
#     print(curposition)

# truncate() function:

with open('myfile.txt','w') as f:
    f.write('hello ! world')
    f.truncate(7)
with open('myfile.txt','r') as f:
    print(f.read())