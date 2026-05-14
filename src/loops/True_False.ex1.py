sum = 0
quant_num = 0
x = 0
while True:
    x = int(input('Enter a integer number:'))
    if x < 0:
        continue #continue makes the restart the loop from the beginning
    if not x: #x is 0 - False, if not x - True (when x is greater than zero)
        break
    sum += x # adds the values to the x variable
    quant_num += 1 #acts like iterator 
average = sum / quant_num
print(f'The average sum of the values is: {average}')
