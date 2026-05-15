def validate_string(question, min, max):
    s1 = input(question)
    size = len(s1)
    while ((size< min) or (size > max)):
        s1 = input(question)
        size = len(s1)
    return s1

x = validate_string ('Enter a string: ', 10, 30)
print(f'You entered the string: {x}. \nValid data. Closing the program ...')