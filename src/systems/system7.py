#Função pára cadastrar livro
def cadastrar_livro(id):
    
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o autor: ')
    ano = int(input('Digite o ano: '))
    isbn = int(input('Digite o ISBN:'))

    livro = {
        'id': id,
        'nome': nome, 
        'autor': autor, 
        'ano': ano, 
        'isbn': isbn
    }

    biblioteca.append(livro)
    print('Livro adicionado com sucesso!')

#Função para listar livros
def listar_livro():

    for livro in biblioteca:
        print(f'ID: {livro['id']}')
        print(f'Nome: {livro['nome']}')
        print(f'Autor: {livro['autor']}')
        print(f'Ano: {livro['ano']}')
        print(f'ISBN: {livro['isbn']}')

#Função para remover livro
def remover_livro():
    id_remover = int(input('Digite o id que deseja remover '))

    for livro in biblioteca:
        if livro['id'] == id_remover:
            biblioteca.remove(livro)
            print('Livro removido com sucesso')
            return #encerra a função assim que o livro for encontrado
    print('Id não encontrado')

biblioteca = []
id_global = 0

while True:
    print('\nMenu')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Remover')
    print('4 - Sair')

    opcao = input('Digite a oção desejada: ')

    if opcao == '1': 
        cadastrar_livro(id_global)
        id_global += 1
    
    elif opcao == '2':
        listar_livro()

    elif opcao == '3':
        remover_livro()
    
    elif opcao == '4':
        print('Programa Encerrado')
        break

    else: 
        print('Opção Inválida')


