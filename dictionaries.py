#this program is to learn about dictionaries
#dictionaries are used to store data values in "key:value" pairs
#key in a dictionary can not store a key, lists,etc. because key in a dictionary should be immutable 
#dictionary is mutable 
info={
    "key":"value",
    "name":"satyam",
    "learning":{"python","c","java"},
    "topic":["sets","dictionaries"],
    "age":35,
    "is_adult":True,
    "marks":94.6
}

print(info)
print(type(info))

#to print a key's value 
print(info["name"])
print(info["age"])

info["name"]="shivam" #this step overwrite the value in the key 
info["surname"]="sharma"

print(info)

#to create null dictionary 
null_dict={}

print(null_dict)

new_dict={
    "city":"kasganj"
}
info.update(new_dict)
print(info)
