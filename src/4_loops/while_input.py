#Validating input data with a loop
x = int(input("Enter a number greater than zero: "))
while (x <= 0): #keeps the loop while the user enter numbers less than zero.
    x = int(input("Enter a number greater than zero: "))
print(f"You entered {x}. Closing the program... ")