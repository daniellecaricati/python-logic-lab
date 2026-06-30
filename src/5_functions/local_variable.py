#def omelet ():
#   eggs = 12 #this is a local variable, only works inside the function omelet
# ------ main program
#omelet ()
#print (eggs)
# we must assign the variable eggs to the main program and bring the print statement into the function
def omelet ():
    print(eggs) #local scope

eggs = 12 #global variable
omelet()
