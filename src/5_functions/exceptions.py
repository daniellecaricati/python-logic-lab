#Exceptions happens when syntax is correct but unexpected errors occurs 
while True:
    try: #forces it to execute 
        x = int(input('Please enter a number:'))
        break
    except ValueError: #name of exception
        print('Oops! Invalid number. Please try again...')
