birth_year = int(input("What is the year of yout birth? "))
year_now = int(input("What year is now? "))
age = year_now - birth_year
print(f'You are {age} years old!')
if (age >= 18):
    print("You are an adult! You can have a driving license now.")
else:
    print("You are underage!")