#Set a default value when creating the function variables. Therefore, if one of the parameters is omitted, the default value is used. 
def sum3 (x = 0, y = 0, z = 0): 
    res = x + y + z
    print (res)

sum3 (1, 2, 3)
sum3 (1, 2) #z omitted
sum3 (1) #y and z omitted
sum3 () #x, y, z omitted

