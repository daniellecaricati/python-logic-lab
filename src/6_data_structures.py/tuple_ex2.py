#function with two parameters, one is a string, the other is arbitrary number of packed numbers. 
#inside the function find the largest of all the received numbers, within the function, the message and the largest value. 
def largest(msg, *num):
    greater = 0
    for i in num:
        if i > greater:
            greater = i 
    print(msg, greater)

largest('The largest number is: ', 8, 6, 4, 78, 56, 12, 9) #calling function and adding parameters