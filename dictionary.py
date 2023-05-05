dic={1:"ram",2:"karan",3:"shyam",4:"mansi"}
print(dic)
print(dic.values())
print(dic.get(3))
print(dic.get(6))
# print(dic[7])give an error
print(dic.keys())
print(dic.items())
print(dic[3])
for keys in dic.keys():
    print(f"the value corresponding to the key {keys} is {dic[keys]}")
for keys,values in dic.items():
    print(f"the value corresponding to the key {keys} is {values}")
    
