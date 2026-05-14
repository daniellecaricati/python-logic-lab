print('Prime numbers from 2 to 99')
for number in range (2, 100, 1):
    flag = 0 #variable to change the value in case it is not a prime number
    for i in range (2, number, 1):
        if( number % i == 0): # if the num is divisible by any value, it is not prime
            flag = 1
            break # in case it finds a number divisible by any value it stops the loop 
    if (flag == 0):
        print (number)