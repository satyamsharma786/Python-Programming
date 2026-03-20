# program to insert an element in any list 
print("PROGRAM TO INSERT AN ELEMENT IN A LIST OF 5 NUMBERS")
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

#at what index user wants to insert an element
idx=int(input("Enter your index choice to insert any element in the list:"))

#what element does the user want to insert in the list
el=int(input("enter your element to be entered:"))

#insertion
numbers.insert(idx,el)

#final output
print("updated number list:",numbers)

#program ended
