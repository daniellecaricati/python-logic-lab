frase = input('Digite uma frase qualquer:')
tam = len(frase) #qtd de caracteres, pegar o tamanho da frase para depois fatiar 

frase2 = frase[:int(tam/2)] # esta pegando do inicio ate a metade dela dividido por 2

print(frase2[-2:]) # mostrar os 2 ultimos caracteres