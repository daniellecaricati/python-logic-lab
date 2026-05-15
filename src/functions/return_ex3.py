def validate_int(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
    return x 

def sum_interval(start, end):
    sum = 0
    i = start
    while 1 <= end:
        sum += i 
        i = i + 1
    return sum 

x = validate_int("Enter an integer and positive number: ", 1, 99999)
y = validate_int('Enter a second integer and positive number: ', 1 , 99999)
print(f'The total sum of {x} and {y} is {sum_interval (x, y)}.')