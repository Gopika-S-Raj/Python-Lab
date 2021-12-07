s=int(input("enter a number"))
fac=1
if s<0:
    print("factorial can not applied")
elif s==0:
    print("factorial of zero is 1")
else:
    for i in range(1,s+1):
      fac=fac*i
    print("factorial of a number is",fac)
