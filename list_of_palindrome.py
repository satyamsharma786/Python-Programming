#this program check if the list contain palindromic elements/ program to check if the list is palindromic or not [hint: use copy()] 

list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list1==list1):
    print(" list 1 is palindrome")
else:
    print("list 1 is not palindrome")
    

if(copy_list2==list2):
    print(" list 2 is palindrome")
else:
    print("list 2 is not palindrome")