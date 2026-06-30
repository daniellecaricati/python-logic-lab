#Unpacking parameter in a function lets the user add as many parameters as needed. 

def quantity (*num): # (*)unpacks the parameters for the variable num
    accumulator = 0
    print ('Tuple: {}'.format(num)) #prints the tuple value
    for i in num:
        accumulator += 1
    return accumulator 

print(f'Result: {quantity(1,2)}\n') #{calling the function}
print(f'Result: {quantity(1,2,3,4,5,6,7,8,9)}\n') #calling the function with parameters 
