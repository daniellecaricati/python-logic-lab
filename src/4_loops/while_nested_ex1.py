age = int(input('What is your age?'))
while (age > 18 ): #executes if the condition is true
    gender = input('What is your gender? (M or F).')
    if ((gender == 'M') or (gender == 'm')):
        print(f'Good evening Sir, your age is {age}.')
    else:
        if ((gender =='F') or (gender == 'f')):
            print(f'Good evening Madam, your age is {age}.')
        else:
            print('Gender option does not exist.')
    age = int(input('What is your age?'))
print('Closing the program...')