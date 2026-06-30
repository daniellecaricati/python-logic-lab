item = [] #empty temporary list
supermarket = []#empty list

for i in range (3): # will loop 3 times
    item.append(input('Enter the name of item: ')) #.append stores it in the item list
    item.append(int(input('Enter the quantity: ')))
    item.append(float(input('Enter the price: ')))
    supermarket.append(item[:]) #copying the item list and storing it in the supermarket list
    item.clear() # to clear the information, so next loop will not add the previous information
print(supermarket)