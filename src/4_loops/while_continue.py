while True:
    name = input("What is your name?")
    if (name != 'Little Lumberjack'):
        continue #Continue makes restart the loop
    password = input('What is the password? ')
    if (password == "Institution"):
        break #stops the loop´
print ('Access granted.')

