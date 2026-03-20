#question 1: print 1 to 10 using for loop 
for i in range(1,11):
    print(i)
    
print("program ended\n")

#question 2: print 10 to 1 using for loop
for j in range(10,0,-1):
    print(j)
     
print("program ended\n")


#question 3: print table of n using for loop 
n=int(input("enter number(n):"))

for k in range(1,11):
    print(n*k)   
print("program ended\n")


#question 4:print a list containing the squares of numbers upto 10 using for loop 
square=[]
for i in range(11):
    square.append(i*i)

print("list is:",square)

for el in square:
    print(el)

print("program ended\n")

#question 5: searching in a tuple using for loop
    
sq=tuple(square) #list conversion into tuple
print("tuple is:",sq)

x=int(input("enter the number you want to search in above tuple:")) #input of number to be searched

idx=0
for el in sq:
    if(el==x):
        print("number found at idx",idx,"\n")
        break
    idx=idx+1
else:
    print("number not found")
    
print("program ended\n")
