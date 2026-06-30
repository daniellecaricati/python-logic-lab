palavras = ('Danielle', 'Rafael', 'Fatima', 'Adriana', 'Fabiana')

#Percorre as palavras na lista
for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais: ') 
    for letra in palavra: #Percorre as vogais de cada palavra
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

            