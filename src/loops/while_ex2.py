#Write an algorithm that obtains an initial and a final value from the user. For this range specified by the user, calculate and display on the screen:
#a. The number of positive integers;
#b. The number of even numbers;
#c. The number of odd numbers;
#d. The respective average of each of the previous items;
#It will be necessary to create a distinct variable for each summation, for each quantity, and for each requested average.
initial = int(input("Enter an initial value: "))
final = int(input("Enter a final value: "))
positive = 0
odd = 0
even = 0
positive_sum = 0
odd_sum = 0
even_sum = 0

i = initial 
if (initial <= final):
    while (i <= final):
        if (i > 0):
            positive = positive + 1
            positive_sum = positive_sum + 1
        if (i % 2 == 0):
            odd = odd + 1
            odd_sum = odd_sum + 1
        else:
            even = even + 1
            even_sum = even_sum + 1
        i = i + 1
    positive_average = positive_sum / positive
    odd_average = odd_sum / odd
    even_average = even_sum / even
    print(f"Total of positive values: {positive}")
    print(f"Average sum of positive values: {positive_average}")
    print(f"Total of odd value: {odd}")
    print(f"Average sum of odd values: {odd_average}")
    print(f"Total of even values: {even}")
    print(f"Average sum of even values: {even_average}")
else:
    print("You entered a inital value greater or equal to the final value. Finishing the system...")
