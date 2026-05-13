print("----CALCULATOR----")
print(" + Addition ")
print(" - Subtraction ")
print(" * Multiplication ")
print(" / Division ")
op = input("Which operation do you want? ")
x = int(input("Enter the 1° number: "))
y = int(input("Enter the 2° number: "))

if (op == "+"):
    res = x + y
    print(f"The result is: {x} + {y} = {res}")
elif (op == "-"):
    res = x - y
    print(f"The result is: {x} - {y} = {res}")
elif (op == "*"):
    res = x * y
    print(f"The result is: {x} * {y} = {res}")
elif (op == "/"):
    res = x / y
    print(f"The result is: {x} / {y} = {res}")
else:
    print("Invalid operation!")