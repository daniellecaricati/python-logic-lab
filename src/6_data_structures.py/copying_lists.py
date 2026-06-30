original_list = [5, 7, 9, 11]
#every list is an object, if we change one, it will change the other simutaneously. 
#copy_list = original_list #this is copying a dependent list 
#copy_list [0] = 2 #it will change both lists

#use [:] to create an Independent list 
copy_list = original_list [:]
copy_list [0] = 2 
print(original_list)
print(copy_list)


