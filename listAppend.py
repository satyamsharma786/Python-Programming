# program to add element to any list 
print("PROGRAM TO ADD ELEMENT IN LIST OF 5 NUMBERS")
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

# adding an element 
print("which element do you want to add in the list ?")
f=int(input("enter f:"))

numbers.append(f)

#output after adding the last element in the list 
print("Updated list of numbers:",numbers)
