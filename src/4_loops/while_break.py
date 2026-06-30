print("Type a message and I will repeat it for you.")
print('To exit, type "exit".')
while True: #while True is infinite loop
    text = input('')
    print(text)
    if text == 'exit':
        break #break ends the loop 
print ('Closing the program...')