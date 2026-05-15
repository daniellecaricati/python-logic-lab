def omelet():
    global eggs #global lets the program manipulate a global variable within a function.
    eggs = 6

eggs = 12
omelet()
print(eggs)