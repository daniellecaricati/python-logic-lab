#Write an algorithm that reads two values ​​and prints the result of their multiplication on the screen. However, to calculate the multiplication, use only addition operations.
x = int(input("Enter the 1º number: "))
y = int(input("Enter the 2º number: "))
cont = 1
mult = 0
while (cont <= x):
    mult = mult + y
    cont = cont + 1
print(f"Result of multiplication: {x} x {y} = {mult}")