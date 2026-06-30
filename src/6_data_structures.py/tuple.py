#Tuple () is static composite variable structure. Acts like arrays. Immutable, can´t modify its values.

bag = ('Jumpers', 'T-shirts','Trousers','Socks','Trainers')
print(bag)
#Searching for elements- Index starts at 0
print(bag[0]) #element 1 - index 0
print(bag[2]) #element 3 - index 2
print(bag[0:2])# elements 1 and 2 - Index 0 and 1
print(bag[2:])#from elements of index 2 to the last 
print(bag[-1])# the last one 

#Scan through the elements of the tuple using a for loop
for item in bag:
    print('There are {} in my bag.'.format(item)) # or   print(f'There are {item} in my bag.')
 