#Função para validar o input do usuario
def valida_int(pergunta, min, max):
    """
    Função para fazer a validação dos dados de entrada do usuario

    """
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


#Função para calcular a fatorial
def fatorial(num):
    """
    Função que calcula a fatorial do numero inteiro
    num : numero inteiro 

    """
    fat = 1 #valor inicial do fatorial e acumulador

    if num == 0:
        return fat 
    
    #executa se num > 0
    for i in range (1, num + 1, 1):
        fat += 1 # fat = fat + 1
    return fat 



x = valida_int('Digite um valor para calcular a fatorial: ', 0, 999)
print (f'{x}! = {fatorial(x)}')