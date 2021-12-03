n=int(input("enter a year>2021"))
if n<=2021:
    print("invalid operation")
for i in range(2021,n+1):
    if i%4==0:
        print(i)
    i=i+1
