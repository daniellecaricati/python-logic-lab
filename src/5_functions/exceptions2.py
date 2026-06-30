def div():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter a number: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Zero Division Error...')
    except:
        print('Something went wrong...')
    else:
        return res
    finally:
        print('It will always execute.')

print(div())