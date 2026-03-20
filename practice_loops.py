#question 1: to find the sum of first N numbers using for loop 
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    sum+=i
    
print("sum is:",sum)

print("program ended\n")

#question 2: same as question 1 but solve by using while loop 
k=int(input("Enter k:"))
sum=0
i=0

while i<=k:
    sum = sum + i
    i =i+1

print("total sum is:",sum)
print("program ended\n")

#question 3:program to find factorial of "n" number
n=int(input("enter n:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1

print("factorial is:",fact)
print("program ended\n")

#question 4:same as question 3 using for loop
n=int(input("enter n:"))
fact=1

for i in range(1,n+1):
    fact *=i
    
print("factorial is:",fact)
print("program ended\n")
