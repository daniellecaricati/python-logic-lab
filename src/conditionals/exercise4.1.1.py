print("Choose what you want to buy:")
print("1 - Apple")
print("2 - Orange")
print("3 - Banana")
product = int(input("Enter the number of your choice."))
quant = int(input("How many do you want?"))
if (product == 1):
    pay = quant * 2.3
    print(f"You bought {quant} apples. Total pay is: {pay}.")
else:
    if (product == 2):
        pay = quant * 3.6
        print(f"You bought {quant} oranges. Total pay is {pay}.")
    else:
        if(product == 3):
            pay = quant * 1.85
            print(f"You bought {quant} bananas. Total pay is {pay}.")
        else:
            print("Invalid product!")