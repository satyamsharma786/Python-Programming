#note: sets are mutable but elements in a set are immutable

collection={1,1,2,3,4,5,2,2,4,"hello","world"}
print(collection)

disk=set() #creation of empty set

#addition of elements in empty set
disk.add(1)
disk.add(2)
disk.add(3)
print(disk)

disk.remove(1) #remove the element 
print(disk)

disk.pop() #removes the random value
print(disk)

unity=disk.union(collection) #union of sets 
print(unity)

intersector=disk.intersection(collection) #intersection of sets
print(intersector)

disk.clear() #clears the set
print(disk)

collection.clear()
print(collection)
