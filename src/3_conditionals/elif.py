name = input("What is your name? ")
age = int(input("What is your age? "))
if name == "Vinicius":
    print("Hello, Vinicius!")
elif age < 18:
    print("You are not Vinicius and you are underage!")
elif age > 100:
    print("Unlike you, Vinicius is not imortal.")