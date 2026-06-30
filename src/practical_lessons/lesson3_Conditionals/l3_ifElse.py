ano = int(input('Digite o ano:'))

if (ano % 4 == 0): #se é divisivel por 4
    print ('Ano bissexto')
else: 
    print('Definitivamente não é um ano bissexto')

print('-' * 20)

cima = True
baixo = True
if( cima == True and baixo == True):
    print('Decida-se')
else:
    print('Voce escolheu um caminho')