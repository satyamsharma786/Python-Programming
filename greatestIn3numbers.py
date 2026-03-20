#program to find the greatest in the 3 numbers input by the user 
print("Program to find the greatest number in the 3 numbers")

# user input 

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

# condition check 
if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
elif(c>a and c>b):
    print("c is greatest")


