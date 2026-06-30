print('Calculadora')
print('Adição +')
print('Subtração -')
print('Multiplicação * ')
print('Divisão /')
print('Digite qualquer tecla para sair')

op = input('Escolha a operação desejada: ')
x = int(input('Digite o 1º valor: '))
y = int(input('Digite o 2º valor: '))

if (op == '+'):
    res = x + y
    print(f'O valor de {x} + {y} = {res}')
elif(op == '-'):
    res = x - y
    print(f'O valor de {x} - {y} = {res}')
elif(op == '*'):
    res = x * y
    print(f'O valor de {x} * {y} = {res}')
elif(op == '/'):
    res = x / y
    print(f'O valor de {x} / {y} = {res}')
else:
    print('Encerrando..')