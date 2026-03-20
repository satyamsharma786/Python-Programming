# program to remove element to any list 
print("PROGRAM TO REMOVE ELEMENTS USING INDEXING FROM ANY LIST OF 5 NUMBERS")
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

#user choice for removal of any element
print("what element do you want to remove from the list ? Note: enter the index from 0 to 4")
idx=int(input("enter index of that element:"))

#removal of any element
numbers.pop(idx)

print("Your updated list is:", numbers)
