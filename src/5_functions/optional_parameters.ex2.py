#We can adapt our summation routine to decide whether we want to print it on the screen by creating an optional parameter.
def sum3 (x = 0, y = 0, z = 0, show = False):
    res = x + y + z
    if show: #if show is true will print the res
        print(res)

sum3 (1 ,2, 3) #as we didnt add the 4º parameter, it will not show the res
sum3 (1, 2, 3, True) # it now shows the res because we have added the 4º parameter 

#To add only two values ​​and still print to the screen, we will need to explicitly state that True refers to the variable show.
sum3 (1, 2 , show =True)