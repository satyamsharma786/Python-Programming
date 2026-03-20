# program to slice any list 
print("PROGRAM TO SLICE A LIST OF 5 NUMBERS")
#declaration
print("To generate a list, enter 5 numbers")

#input of values 5 elements
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
e=int(input("enter e:"))

#list of all elements 
list=[a,b,c,d,e]

print("Your values:",list)

#slicing choice
print("from index 0 to 5 choose lower limit and upper limit")

up=int(input("Upper limit:"))
low=int(input("lower limit:"))

#output of sliced list
print("Sliced list is:",list[up:low])

#program ended

