#program to check if a list contain any palindrome number 
#user input two lists

#input of list 1
print("enter 3 values for list 1:")
a=int(input("value 1:"))
b=int(input("value 2:"))
c=int(input("value 3:"))

#list 1
list_1=[a,b,c]
print(list_1)

copy_list1=list_1.copy

if(copy_list1==list_1):
    print("palindrome")
else:
    print("not palindrome")

#program ended
