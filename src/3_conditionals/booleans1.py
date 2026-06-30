a = 1
b = 2
c = 3
x = 20
y = 10
z = -1
v1 = True
v2 = False
name = "Peter"
address = "Little Peter"
print( a + c / b)
print ( c / b / a)
print (-x ** b)
print (v1 or v2) #True
print(v1 and not v2) #True
print(v2 and not v1) #False
print(not name == address) #is name equal to address ? False, change value to True
print(v1 and not v2 or v2 and not True) #1º not v2 = True, 2º not True = False, 3º v1 and not v2 = true,4º v2 and not True = False , 5º or = True
print (x > y and c <= b)
print (c - 3 * a < x + 2 * z) # 3*1 = 3, 2*-1 = -2, c - 3 = 0, 20+ (-2)= 18