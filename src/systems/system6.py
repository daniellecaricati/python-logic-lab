#função para criar o dicionario 
def cadastrar_livro(titulo, autor, ano, isbn):
    livro = {
        'titulo': titulo, 
        'autor': autor,
        'ano': ano,
        'isbn': isbn
    }
    return livro

biblioteca = []
titulo = input('Titulo: ')
autor = input('Autor: ')
ano = int(input('Ano: '))
isbn = int(input('ISBN: '))

livro = cadastrar_livro(titulo, autor, ano, isbn)
biblioteca.append(livro.copy())