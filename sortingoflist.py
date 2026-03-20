# program to sort any list 
print("PROGRAM TO SORT A LIST OF 5 NUMBERS")
#declaration
print("To generate a list, enter 5 numbers")

#input of values 5 elements
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
e=int(input("enter e:"))

#list of all elements 
numbers=[a,b,c,d,e]
print("Your values:",numbers)

#user choice to input what type of sorting does he want
print("what type of sorting do you want ?")
print("available options\n  1.ascending order sort\n  2.descending order sort\n  3.reversing sort")

#user input sort choice
user=int(input("Enter your choice of sorting: "))

#condition check
if(user==1):
    numbers.sort()
    print(numbers)
elif(user==2):
    numbers.sort(reverse=True)
    print(numbers)
elif(user==3):
    numbers.reverse()
    print(numbers)
else:
    print("Invalid option entered by the user.")


#program ended