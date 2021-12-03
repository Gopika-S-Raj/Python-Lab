l=[]
n=int(input("enter total number of in the list elements:"))
(input("enter the elements"))
for i in range (1,n):
    element=int(input())
    if element>=100:
        l.append("over")
    else:
        l.append(element)
print(l)
