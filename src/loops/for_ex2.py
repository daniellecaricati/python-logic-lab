num = int(input('Enter a number to calculate the multiplication table:'))
print (f'Multiplication table of {num}:')
for i in range (1, 11, 1):
    print (f'{i} x {num} = {i * num}')