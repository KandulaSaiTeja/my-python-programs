#prime number
x=int(input("enter the number:"))
k=0
for i in range(1,x+1):
    if x%i==0:
        k=k+1
if k==2:
        print("prime number")
else:
        print("not a prime number")
        
