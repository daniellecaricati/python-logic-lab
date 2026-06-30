def greater3(v1 = 0, v2 = 0, v3 = 0):
    if (v1 and v2 and v3):
        if ((v1 > v2) and (v1 > v3)):
            if (v2 > v3):
                print(f'Ascending order: {v3}, {v2}, {v1}')
            else: 
                print(f'Ascending order: {v2}, {v3}, {v1}')
        elif ((v2 > v1) and (v2 > v3)):
            if (v1 > v3):
                print (f'Ascending order: {v3}, {v1}, {v2}')
            else: 
                print(f'Ascending order: {v1}, {v3}, {v2}')
        elif ((v3 > v1) and (v3 > v2)):
            if (v1 > v2):
                print(f'Ascending order: {v2}, {v1}, {v3}')
            else:
                print(f'Ascending order: {v1}, {v2}, {v3}')

x = int(input('Enter the 1º value: '))
y = int(input('Enter the 2º value: '))
z = int(input('Enter the 3º value: '))
greater3 (x, y, z)