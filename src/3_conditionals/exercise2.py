salary = float(input("What is your salary?"))
admission_year = int(input("What year was your admission?"))
year_now = int(input("What year is now?"))
time_admission = year_now - admission_year
if (time_admission > 5): #executes if condition is true
    bonus = salary * 0.2
else:
    bonus = salary * 0.1
print(f"You have {time_admission} of years in this company.")
print(f"Your salary is {salary}.")
print(f"Your bonus is {bonus}.")
print(f"Your final salary is {bonus + salary}.")