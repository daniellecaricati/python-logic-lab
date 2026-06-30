#Lists [] is a composite variable that allows you to modify its data.
bag = ['Banana', 'Avocado','Apple', 'Strawberry', 'Lemon','Pinapple']
print('List:', bag)

#To modify a list
bag[2] = 'Orange'
print('Modified List:', bag)

#to add an item to the end of the list only - use append() method
bag.append('Egg')
print('Added item to the end of the list:', bag)

#to add an item to any position of the list - use insert() method
bag.insert(1,'Lettuce')
print('Added item to index 1 of the list:', bag)

#to remove an item stored in any index of the list
del bag[1]
print('Deleted item stored in index 1 of the list.', bag)

#to delete the informed item - use remove() method
bag.remove('Egg') 
print ('Deleted the informed item:', bag)

#Methods - variablename.methodname(parameter)