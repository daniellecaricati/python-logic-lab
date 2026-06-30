print('-'*10, 'Tuple', '-'*10)
bag = ('Banana', 'Avocado', 'Strawberry', 'Apple', 'Orange')
# to add items to the existing tuple, you have to create another tuple and concatenate them.
upgrade = ('Cheese', 'Ice Cream', 'Brownie')
bag_upgrade = bag + upgrade
print(bag)
print('-'*10, 'Adding Tuple', '-'*10)
print(upgrade)
print('-'*10, 'Concatenated Tuples', '-'*10)
print(bag_upgrade)
#the order you concatenate them matters. 
inverted_bag = upgrade + bag
print('-'*10, 'Inverted tuple', '-'*10)
print(inverted_bag)