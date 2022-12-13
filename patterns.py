"""x=int(input())
# right angle triangle
print("right angle triangle")
for i in range(x):
    print(" "*(x-1)+"*"*(i+1))
# left angled triangle
print("left angled triangle")
x=int(input())
for i in range(x):
    print(" "*(x-i)+"*"*(i+1))
# inverted left angled triangle
print("inverted left angled triangle")
x=int(input())
for i in range(x):
    print(" "*i+"*"*(x-i))
# inverted right angled triangle
print("inverted right angled triangle")
x=int(input())    
for i in range(x):
    print("*"*(x-i))
print("combination of right angles triangle with * and inverted left angled triangled with-")    
# combination of right angled triangle with * and iverted left angle triangle with - 
x= int(input())    
for i in range(x):
    print(" "*(x-1)+"*"*(i+1),"-"*(x-i))
print("rectangle")    
# we can form rectangle l*b b greater then l
x=int(input())
for i in range(x):
    print("*"*(x))
#x=int(input())
print("number format")
x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
        if i>j and i!=j:
             print("*",end="")
    print()
for i in range(x-1,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
        if j>i and j!=i:
              print("*",end="")
        
    print() """       
# Numbers pattern
x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
# Number pattern
x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    
