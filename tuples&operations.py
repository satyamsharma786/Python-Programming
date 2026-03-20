#tuples and its operations like indexing and ocuurence counting
print("PROGRAM TO WORK WITH TUPLES")

#user enters the values for tuples 
print("CREATING TUPLE FOR 5 ELEMENTS")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
e=int(input("enter e:"))

#creation of tuple
tuple=(a,b,c,d,e)
print("your created tuple is:",tuple)

#user inputs the element for operations
el=int(input("enter the element for doing operations:"))

#operations on tuples 1.indexing any element & 2.counting occurence of any element
print("operations available\n  1.indexing element\n  2.counting occurence")

#user choice
ip=int(input("enter operation choice:"))

#logic for operations
if(ip==1):
    tuple.index(el)
    print("index of your element is:",tuple.index(el))
elif(ip==2):
    tuple.count(el)
    print("occurence of your element is:",tuple.count())
else:
    print("invalid option entered")

#program ended