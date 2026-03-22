print("Welcome to our CLI based calculator.\n Note:This will work for only two numbers.")
print("Enter number a:")
a=int(input())
print("Enter number b:")
b=int(input())

#Menu (add/subtract/multiply/devide)
print("Available Options:\n 1.Add\n 2.Subtract\n 3.Multiply\n 4.Devide\n 5.Power")
print("Enter your choice number:")
choice=int(input())

#define functions
def sum():
    sum=a+b
    print("sum is",sum)

def diff():
    diff=a-b
    print("difference is",diff)
    
def multi():
    multi=a*b
    print("multiplication is",multi)
    
def dev():
    dev=a/b
    print("devide is",dev)
    
def pw():
    pw=a**b
    print("powered calculation is",pw)

if choice==1:
    sum()
elif choice==2:
    diff()
elif choice==3:
    multi()
elif choice==4:
    dev()
elif choice==5:
    pw()
else:
    print("Invalid option entered by you......")