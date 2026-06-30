print(' -- Lanchonete --')
print(' 1 - Coxinha - R$ 5,00')
print(' 2 - Pastel - R$ 7,00')
print(' 3 - Café - R$ 3,00')
print(' 4 - Suco - R$ 6,00')
print(' 5 - Sair')

total = 0 #Variavel para acumular
while True: 
    produto = int(input('Selecione o produto: '))

    if (produto == 1):
        qtd = int(input('Digite a quantidade: '))
        total = total + qtd * 5.00 #acumulador/iterador
    
    elif (produto == 2):
        qtd = int(input('Digite a quantidade: '))
        total = total + qtd * 7.00
    
    elif (produto == 3):
        qtd = int(input('Digite a quantidade: '))
        total = total + qtd * 3.00
    
    elif (produto == 4):
        qtd = int(input('Digite a quantidade: '))
        total = total + qtd * 6.00
    
    elif (produto == 5):
        break

    else: 
        print('Produto invalido')
    
print(f'Total a ser pago: R$ {total}')