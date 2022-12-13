# code to print biggest number
data=input().split()
i = data[0]
for x in data:
    if x > i:
        i = x
print("biggest number=",i)
# code to print smallest number
for y in data:
    if y < i: 
        i = y
print("smallest number",i)
