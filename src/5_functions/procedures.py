#A function is a routine that returns values ​​associated with its name. It can be used in assignments or even in logical expressions.
#routines that contain or not parameters, but never return any data are called Procedures.
def sum3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res 

returned = sum3(1, 2, 3)
print(returned)
print(sum3(2,2))
print('-' * 30)
returned1 = sum3 (1 ,2 ,3)
returned2 = sum3(1,2)
returned3 = sum3()
print(f'Total sum: {returned1}, {returned2} and {returned3}.')