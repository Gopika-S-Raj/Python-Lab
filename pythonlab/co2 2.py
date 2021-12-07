print("enter the term")
n=int(input())
n1,n2=0,1
count=0
if(n<=0):
    print("fibanacci series can not applied")
elif(n==1):
    print("fibanacci series is",n1)
else:
    print("fibanacci series is",)
    while(count<n):
        print(n1)
        a=n1+n2
        n1=n2
        n2=a
        count+=1
        
  
