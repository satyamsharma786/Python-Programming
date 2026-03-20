#to find occurence in a string using str.count() command 
string=str(input("enter your full name:"))
print("which letter are you trying to find in your name ?")
user=input("enter your word:")
occurence=string.count(user)
print("occurence is:",occurence)
