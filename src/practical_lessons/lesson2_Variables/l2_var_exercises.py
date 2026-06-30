#1 - O somatório dos 5 primeiros numeros inteiros e positivos
print(' 1: ', 1 + 2 + 3 + 4 + 5)

#2 - A média entre 23, 19 e 31
print(' 2: ',(23 + 19 + 31) // 3 ) # // Divisão somente com a parte inteira

# 3 - O numero de vezes que 73 cabe em 403
print (' 3: ', 403 // 73)

# 4 - A sobra quando 403 é dividido por 73 
print (' 4: ', 403 % 73) # % modulo - resto da divisão

# 5 - 2 elevado à 10ª potencia 
print (' 5: ', 2 ** 10) # ** - exponenciação

# 6 - O valor absoluto da diferença entre 54 e 57 (valor avsoluto é sem o sinal - no resultado)
print (' 6: ', abs(54 - 57)) # abs faz pegar o valor absoluto 

# 7 - O menor valor entre 34, 29, 31 
print (' 7: ', min(34, 29, 31)) #min pega o menor valor 

# 8 - Atribuir o valor inteiro 3 a variavel A
a = 3

# 9 - Atribuir o valor inteiro 4 a variavel B
b = 4

# 10 - Atribuir a variavel C o valor da expressao a * b + b * b
c = a * a + b * b
print ('10: ', c )

# 11 - execute as atribuições s1 = "ant", s2 = "bat", s3 = "cod", utilize + e * e crie saidasa seguir;
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
res = s1 + ' ' + s2 + ' ' + s3
print ('11 - a:', res)

res1 = 10 * (s1 + ' ')
print ('11 - b:', res1)

res2 = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print ('11 - c:', res2)

res3 = ((s1 + ' ') + (s2 + ' ')) * 7
print ('11 - d:', res3)

res4 = ((s2 * 2) + s3 + ' ') * 5
print ('11- e:', res4)