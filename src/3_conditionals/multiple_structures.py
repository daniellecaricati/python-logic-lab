salary = float(input("Enter your salary: "))
admission = int(input("When were you admitted?: "))
year_now =int(input("What year is now? "))
time = year_now - admission
if (time > 10):
    bonus = salary * 0.3 # 30%
else:
    if (time > 5):
        bonus = salary * 0.2
    else: 
        bonus = salary * 0.1
print(f"You have been working in this company for {time} years.")
print(f"Your salary is {salary}.")
print(f"Your bonus is {bonus}.")
print(f"Your final salary is: {bonus + salary}.")