a=[]
n=int(input("enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("enter element:"))
    a.append(element)
b=set()
unique=[]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("non-duplicate items:")
print(unique)
