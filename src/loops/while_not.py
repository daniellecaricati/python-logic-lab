#Truthy and Falsey
name = '' #Empty String = Falsey
while not name: #Change the value of name= False to True / same as While True
    name = input('Enter your name: ') #stops the loop when name is fulfilled
value = int(input('Enter a number: '))
if value: # Same as if value != 0:
    print('You entered a value other than zero.')
else:
    print('You entered zero.')