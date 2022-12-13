#check if the given string is palindome or not
x= str(input("enter:").lower())
revx=""
for i in x:
    revx=i+revx
if x==revx:    
    
    print("palindrome")
else:
    print("not a palindrome")
