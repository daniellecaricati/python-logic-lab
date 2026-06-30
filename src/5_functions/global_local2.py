def omelet():
    eggs = 12 #local variable of omelet
    print('Eggs = ', eggs)

def bacon ():
    eggs = 6 #local variable of bacon
    print('Eggs = ', eggs) #will print 6
    omelet() #calls omelet function , where egg = 12, will print 12
    print('Eggs = ', eggs) # will print 6

eggs = 2 #global variable
bacon() #calling bacon function
print('Eggs = ', eggs) #prints the global variable

