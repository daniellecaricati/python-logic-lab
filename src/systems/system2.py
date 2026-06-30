biblioteca = []

#Cadastro da função
def cadastrar_livro():
    print("Cadastro de Livro")

   
    titulo = input("Digite o titulo: ")
    autor = input("Digite o autor: ")
    isbn = input('Digite o ISBN: ')
    ano = input("Ano de publicação: ")
    #Criando o dicionario
    livro = { 
        'titulo' : titulo,
        'autor' : autor,
        'isbn'  : isbn,
        'ano' : ano
    }
    #Adicionando o dicionario na lista
    biblioteca.append(livro.copy())

#chamada da função
cadastrar_livro()

#Percorre a lista e exibe o conteudo
for livro in biblioteca:
    print(f'Livro adicionado : {livro}')
