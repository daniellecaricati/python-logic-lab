i = 10
while (i < 20):
    for j in range (10, 20, 2):
        print('{} + {} = {}' .format(i, j, i+j))
    i += 1 #Incremento do passo

print ('-'*20)

for i in range (10, 20): #(inicio 10, final 20, passo 1)
    for j in range (10, 20, 2): #inicio(10, final 20, passo 2)
        print('{} + {} = {}' .format(i, j, i+j))