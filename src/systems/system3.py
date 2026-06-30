biblioteca = []

def cadastrar_livro():
    #Solicita dados
    titulo = input("Digite o titulo: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano: ")
    isbn = input("Digite o isbn: ")

    #Verifica se ISBN ja existe
    for livro in biblioteca:
        if livro['isbn'] == isbn:
            print('Erro. Ja existe um livro com este isbn')
            return
    
    #Cria o dicionario do livro
    novo_livro = {
        'titulo' : titulo, 
        'autor': autor,
        'ano': ano,
        'isbn': isbn
    }
    #Adiciona o dicionario na lista
    biblioteca.append(novo_livro.copy())
    print('Livro cadastrado com sucesso')


def pesquisar_livro():
    print('Pesquisar livro')
        #pesquisar por titulo
    titulo_busca = input("Digite o titulo do livro").lower()
    encontrado = []
    for livro in biblioteca:
        if titulo_busca in livro['titulo'].lower():
            encontrado.append(livro)

    if encontrado:
        print(f'{len(encontrado)}')
        for i, livro in enumerate(encontrado, 1):
            print(f'Titulo: {livro['titulo']}')
            print(f'Autor: {livro['autor']}')
            print(f'ano: {livro['ano']}')
            print(f'isbn: {livro['isbn']}')
    else:
        print('Nenhum livro encontrado com esse titulo ')


def remover_livro():
    print(f'Remover livro')
    isbn_remover = input('Digite o ISBN que deseja remover: ')

    for i, livro in enumerate(biblioteca):
        if livro['isbn'] == isbn_remover:
            print(f'Livro encontrado ')
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")

            #Confirmação antes de excluir
            confirmar = input("Deseja realmente remover este livro? ").lower()
            if confirmar == 's':
                biblioteca.remove(i)
                print('Livro removido com sucesso')
            else:
                print('Operação Cancelada')
            return
        
    print('Livro não encontrado com esse isbn')

def listar_livro():
    print('Listar todos os livros')
    if not biblioteca:
        print('Biblioteca vazia')
        return
    
    print(f'Total de livros : {len(biblioteca)}')
    for i, livro in enumerate(biblioteca, 1):
        print(f'{i} - {livro['titulo']}, {livro['autor']}, {livro['isbn']}, {livro['ano']}')


def menu_principal():
    while True:
        print('MENU PRINCIPAL')
        print('1 - Cadastrar livro')
        print('2 - Pessquisar livro')
        print('3 - Remover livro')
        print('4 - Listar livro')
        print('5 - Sair')

        opcao = input('Digite a opcao desejada: ')
   
        if opcao == '1':
            cadastrar_livro()
        
        if opcao == '2':
            pesquisar_livro()
        
        if opcao == '3':
            remover_livro()
        
        if opcao == '4':
            listar_livro()
        
        if opcao == '5':
            break

menu_principal()


