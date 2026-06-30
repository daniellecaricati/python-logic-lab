total = 0 # var para acumular total de pessoas/ingressos
dinheiro = 0 #var para acumular valor dos ingressos
acc_idade = 0 #var para acumular idades

while True:
    idade = int(input("Qual sua idade? "))
    if idade == 0:
        break

    total += 1
    acc_idade += idade
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

if total > 0:
    media = idade / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Média arrecadada: {media}')