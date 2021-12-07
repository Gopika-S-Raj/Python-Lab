l=[1,3,6,4]
l2=[1,3,4]
print("l1=",l)
print("l2=",l2)
if len(l)==len(l2):
    print("lists are of same length")
else:
    print("lists are not of same length")
if sum(l)==sum(l2):
    print("sums are equal")
else:
    print("sums are not equal")
print(set(l).intersection(l2))
