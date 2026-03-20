grades=("C","D","A","A","B","B","A")
print("given tuple of grades:",grades)

#user input the grade that he wants to count
user_input=input("Enter your grade you want to count in the tuple (note:use capital alphabets in input):")

grades.count(user_input)

print("your count is:",grades.count(user_input))
