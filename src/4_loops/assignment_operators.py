# Assingment operators: +=, -=, *=, /=, **=, //=

x = 1
while (x <= 5):
    print(x)
    x += 1 # This is equivalent to : x = x + 1
print("-" * 30)
sum = 0
cont = 1
while (cont <= 5):
    x = int(input(f"Enter the {cont}º number: "))
    sum += x #Equivalent to : sum = sum + x
    cont += 1 #Equivalent to: cont = cont + 1
print(f"Total sum: {sum}")