#practice questions on sets
print("=====QUESTION 1=====")
#question 1: create a dictionary to store word meanings in it 
dictionary={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(dictionary)

print("=====QUESTION 2=====")
#question 2: given the subjects and we have to find the number of classrooms for each subjects
subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

print("=====QUESTION 3=====")

#question 3:storing user input the subject and its marks in a dictionary 
marks={}

x=int(input("enter phy:")) #input of subject marks
marks.update({"phy":x}) #dictionary updation

y=int(input("enter math:"))
marks.update({"maths":y})

z=int(input("enter chem:"))
marks.update({"chem":z})

print(marks) #output of dictionary 

print("*****program ended*****")