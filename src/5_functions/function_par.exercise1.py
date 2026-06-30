def border (s1):
    size = len(s1)
    if size: #only prints in case there is a character
        print('+', '-' * size,'+')
        print('|', s1, '|')
        print('+', '-' * size,'+')

border('Hello World')
border('Programming Logic and Algorithm')