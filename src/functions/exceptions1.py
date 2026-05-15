i = 1
while True:
    try: 
        name = input('Please enter your name: ')
        ind = int(input('Enter a index of the name given: '))
        print(name[ind])
        break
    except ValueError:
        print('Oops! Invalid name. Please try again..')
    except IndexError:
        print('Oops! Invalid index. Please try again..')
    finally: #finally will happen anyways . Here it is used to increment the counter
        print(f'Try: {i}')
        i += 1