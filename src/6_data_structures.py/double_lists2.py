#Different code but the same output as double_indexing3
supermarket = [] #empty list

for i in range(3): #will loop 3x
    name = input('Enter name of item: ')
    quant = int(input('Enter the quantity: '))
    price = float(input('Enter the price: '))
    supermarket.append([name, quant, price]) #inserting the variables in the supermarket list

print(supermarket)
#accessing the items and characters of the lists
#What is the first product?
print(supermarket [0][0])
#What is the price of apple?
print(supermarket [1][2])
#How many pinapples were bought?
print(supermarket[2][1])
print()

#printing the supermarket list showing each column and total price. 
sum = 0
print ('Supermarket list: ')
print('-' * 20)
print('item | quantity | price | total price of item')
for item in supermarket:
    print('{} | {} | {} | {} |'.format(item[0], item[1], item[2], item[1] * item[2]))
    sum += item[1] * item [2]
print('-' * 20)
print(f'Total due: {sum}')