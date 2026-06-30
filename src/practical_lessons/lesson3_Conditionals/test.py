print ('-- Calculadora -- ')
print(' +  Adição')
print(' -  Subtração')
print(' *  Multiplicação')
print(' /  Divisão')

operacao = input('Qual operação deseja realizar? ')
x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))

if (operacao == '+'):
    res = x + y
    print(f'{x} + {y} = {res}')

elif (operacao == '-'):
    res = x - y
    print(f'{x} - {y} = {res}')

elif (operacao == '*'):
    res = x * y
    print(f'{x} * {y} = {res}')

elif (operacao == '/'):
    res = x / y
    print(f'{x} / {y} = {res}')

else:
    print('Operação invalida.')