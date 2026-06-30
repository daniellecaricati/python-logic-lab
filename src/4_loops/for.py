#for is used when you know in advance the number of loops you want to repeat. 
# for <var> in range (<start>,<end>,<increment>)
for i in range (6):
    print (i) #I is the control variable, always starts with zero.
print ("-" * 20)
for i in range (1, 6, 1): # 1 = initial value of iterator, 6 = final value of iterator, 1 = iterator step
    print(i)
print("-" * 20)
for i in range (10, 0, -2): # starts at 10, ends at 0, - 2 step 
    print (i)
