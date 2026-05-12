print("Not")
x = 10
y = 1
answer = not x > y #x is greater than y? True. Change the value of True to False.
print (answer)
print("-" * 20)
print("And")
x = 10
y = 1
z = 5.5
answer = (x > y) and (z == y) # And needs both to be True to print True. x is greater than y? True. z is igual to y? False.
print (answer)
print("-" * 20)
print("Or")
x = 10
y = 1
z = 5.5
answer = (x > y) or (z == y) #prints True if one of the conditions is True.
print (answer)
print("-" * 20)
x = 10
y = 1
z = 5.5
answer = x > y or not z == y and y != y + z / x #1º z/x (5.5/10=0.55), 2º - y + z(1 + 0.55 = 1.55) , 3º x > y (10 > 1 = True),
#4º z == y (0.55 ==1) False, 5º y != 1.55 (1 != 1.55) True, 6º not False =True, and (True and True) = True, or (True or True) = True 
print (answer)