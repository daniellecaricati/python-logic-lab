import random

#Função Validação dados
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Função para definir o vencedor
def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 ==1: #Pedra
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:#Papel
            v2 +=1 #Vitoria jogador 2 -> v2 +=1 
        elif jogador2 == 3:#Tesoura
            v1 += 1
    elif jogador1 == 2: 
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3:
            v2 += 1
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3:
            empate += 1

    resultados = [v1, v2, empate]
    return resultados


#Programa principal
print('***JOKENPO***')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
resultados = []

while True:
    j1 = valida_int('Escolha sua jogada', 0, 3)
    if not j1:
        break 

    j2 = random.randint(1,3) #função que gera um numero aleatorio no intervalo desejado
    jogadas.append([j1, j2])#adiciona os jogadores na lista
    resultados = vencedor(j1, j2)

for jogada in jogadas: 
    for dado in jogada:
        print(dado, end=' ')

print(f'Numero de vitorias do jogador 1: {resultados[0]}')
print(f'Numero de vitorias do jogador 1: {resultados[1]}')
print(f'Numero de empates: {resultados[2]}')