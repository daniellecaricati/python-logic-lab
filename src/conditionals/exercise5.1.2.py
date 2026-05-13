print("Payment")
print("1 - Direct Debit")
print("2 - Credit Card 3x")
print("3 - Credit Card 5x")
print("4 - Credit Card 10x")
print("Enter any letter to leave...")
op = int(input("How do you want to pay?"))
value = float(input("What is the price of the product? "))

if (op == 1):
    final_value = value * 0.95
    print(f"Product paid by direct debit. Total: {final_value}")
elif (op == 2):
    final_value = value
    monthly_pay = final_value / 3
    print(f"Product paid by credit card 3x. Total: {final_value}. Monthly pay: {monthly_pay:.2f}")
elif (op == 3):
    final_value = value * 1.02
    monthly_pay = final_value / 5
    print(f"Product will be paid in 5 installments. Total to pay : {final_value}. Monthly pay: {monthly_pay:.2f}")
elif (op == 4):
    final_value = value * 1.08
    monthly_pay = final_value / 10
    print(f"Product will be paid in 10 installments. Total to pay: {final_value}. Monthly pay: {monthly_pay:.2f} ")
else:
    print("Invalid Option.")