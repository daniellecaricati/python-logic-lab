# 2x while
table = 1 #start
while table <= 10: #end
    print (f'Multiplication table of {table}:')
    i = 1 #step/iterator
    while i <= 10: 
        print(f'{table} x {i} = {table * i}')#multiplicator
        i += 1
    table += 1