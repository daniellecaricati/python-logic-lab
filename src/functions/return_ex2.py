def validate_int(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
    return x

def factorial (num):
    fact = 1 
    if num == 0:
        return fact
    for i in range (1, num+1, 1):
        fact *= i

x = validate_int('Enter a value to calculate the factorial: ', 0, 99999)
print(f'{x} != {factorial(x)}.')