start = int(input("What value do you want to start the count with?"))
end = int(input("What value do you want to end the count with?"))
x  = start
while (x <= end):
    if (x % 3 == 0):
        print(x)
    x = x + 1
