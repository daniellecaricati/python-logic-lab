biblioteca = [] #lista vazia

def cadastrar_livro(): #função para receber dados e retornar em dicionario
    titulo = input('Digite o titulo: ')
    autor = input('Digite o autor: ')
    ano = int(input('Digite o ano: '))
    estoque = int(input('Digite a quantidade: '))

    return {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'estoque': estoque
    }

while True: #pergunta quantas vezes o usuario quer cadastrar
    livro = cadastrar_livro() #função de cadastro é inserida em uma variavel 
    biblioteca.append(livro.copy()) #o dicionario é inserido na lista

    continuar = input('Voce deseja cadastrar outro livro? (s/n)') #resposta é inserida no continuar

    if continuar.lower() == 'n': #se a resposta for não, encerra o laço
        break

print('Livros cadastrados: ')
print(biblioteca ) #mostra os livros cadastrados

for livro in biblioteca: #percorrer a lista para mostrar quantidade em estoque
    print(f'{livro['titulo']} - {livro['estoque']}unidades')


titulo_remover = input('Digite o titulo que deseja remover: ')
for livro in biblioteca: # remove um livro 
    if livro['titulo'] == titulo_remover:
        biblioteca.remove(livro)
        print('livro removido')
        break 