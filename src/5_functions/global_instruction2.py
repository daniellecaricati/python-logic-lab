def omelet():
    global eggs #3º indicates eggs is a global variable
    eggs = 6 #4º the global variable eggs (4) is changed to (6)
    bacon() #5 º calling bacon

def bacon():
    eggs = 12 #6º local variable created
    pepper()#7º calling pepper

def pepper():
    print(eggs) #8º prints eggs, as we havent created a new local variable, eggs has the last value assigned (6)

eggs = 4 #1º global variable
omelet() #2º calling eggs
print (eggs) # 9º print eggs (6) because the function omelet has defined eggs as a global variable with a value of 6