l=[2,4,5,6,-7,-6,-3]
for i in l:
    if i>0:
        print(i,end=" ")
s=[x for x in[20,34,53,35] if x%2==0]

s={x:x**2 for x in range(1,11)}
print(s)
v=['a','e','i','o','u']
s=input("enter a string:")
d=[x for x in s if x in v]
print(d)
c=input("enter the string")
list=[]
for i in c:
    list.append(ord(i))
print(list)
