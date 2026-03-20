#question 1: printing 1 to 100
i=0
while(i<=100):
    print(i)
    i=i+1
print("****program__ended****\n\n")


#question 2: printing 100 to 1
j=100
while(j>=1):
    print(j)
    j=j-1
print("===program**ended===\n\n")


#question 3: print table of number N entered by user
print("program of table")
n=int(input("Enter the number you want to find table:"))
i=1
while(i<=10):
    print(n*i)
    i=i+1
print("program ended\n\n")

#question 4:write a program to create a list of squares upto 10.
squares=[]
i=1
while(i<=10):
    a=i*i
    i=i+1
    squares.append(a)
    
print(squares)
print("program ended\n\n")


#question 5: creating a tuple of squares and finding a number in that tuple using while loop 
sq=tuple(squares)

n=int(input("enter the number you gonna find in the tuple of squares upto 10:"))

i=0
while(i<len(sq)):
    if(sq[i]==n):
        print("Found at idx",i)
    
    i=i+1

print("program ended\n")
