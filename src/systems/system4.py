#Função responsavel apenas por pegar dados do usuario e retorna um dicionario
def cadastrar_livro():
    titulo = input('Digite o titulo: ')
    autor = input('Digite o autor: ')
    ano = int(input('Digite o ano: '))

    return {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }

#lista vazia que recebera o dicionario
biblioteca = [] 

#função é inserido na variavel livro
livro = cadastrar_livro()

#livro que agora é um dicionario, é inserido na lista 
biblioteca.append(livro.copy()) 

print(biblioteca)