#this program is based on nesting in dictionaries
#nested dictionary- a key can also be a dictionary example is given below:

student={
    "name":"satyam",
    "subjects":{
        "phy":24,
        "chem":35,
        "math":67,
    }
}

print(student) #to print dictionary

print(student["subjects"])  #to print the nested key from the main dictionary 

print(student["subjects"]["phy"]) #to print specific key from nested key


#METHODS IN DICTIONARIES

#1) myDict.keys()  = return all keys
#2) myDict.values()  = return all values
#3) myDict.items()  = return all (key,value) pairs as tuple
#4) myDict.get("key")  = return all keys according to the value
#5) myDict.update(newDict)  = insert the specified items to the dictionary
