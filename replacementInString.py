#replacing any string 
print("Program for replacement in string")
str=input("enter your string:")

print("what do you want to replace ?")
old=input("To be replaced:")
print("by what do you want to replace with ?")
new=input("with whom to be replaced:")

#replacement logic 
str=str.replace(old,new)
print(str)