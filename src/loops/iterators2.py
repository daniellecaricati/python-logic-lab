sum = 0
count = 1
while (count <= 5):
    x = float(input(f"Enter the {count}º number: ")) #the number will be stored in count and assigned to x 
    sum = sum + x # the sum is 0 + the x 
    count = count + 1 # iterator , increments 1 each loop
print(f"The total sum is: {sum}")
average = sum / 5
print(f"The average is : {average}")