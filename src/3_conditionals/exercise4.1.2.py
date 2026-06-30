a = int(input("Enter the 1º side of triangle: "))
b = int(input("Enter the 2º side of triangle: "))
c = int(input("Enter the 3º side of triangle: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a: #if it executes here is because it is a valid triangle.
        if a != b and a != c and b != c:
            print("It is a scalene triangle.")
        else:
            if a == b and a == c and b == c:
                print ("It is an equilateral triangle.")
            else:
                print("It is an isosceles triangle.")
    else:
        print("At least one of the values is not valid to create a triangle.")   
else: 
    print("At least one of the values is not valid to create a triangle.")             