#Even and odd with functions
def even_odd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
#asking the user, adding the information to the function and printing it. Execution: 1º input, 2º int, 3º even_odd, 4º print.
print(even_odd(int(input('Enter an integer number: ')))) 