def validate_int(question, min, max):
    x = int(input(question))
    while ((x < min) or (x > max)):
        x = int(input(question))
    return x 

x = validate_int('Enter an integer number: ', 0 , 100)
print(f"You entered {x}. Closing the program...")
