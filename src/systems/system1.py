#Resolução Exercicio 4 - Sistema Biblioteca
#Lista para armazenar todos os livros
lista_livros = []

#Substituir pelo RU
id_global = 1000

#Função para cadastrar livros
def cadastrar_livro(id):
    print("\n --- Cadastrar Livro ---")
    nome = input("Digite o nome do livro ")
    autor = input("Digite o autor do livro ")
    editora = int(input("Digite a editora "))

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    lista_livros.append(livro.copy())
    print("Livro Cadastrado com Sucesso")

#Função Consultar Livros
def consultar_livro():
    while True:
        print("---Consultar Livro ---")
        print("1 - Consultar todos")
        print("2 - Consultar por ID")
        print("3- Consultar por autor")
        print("4- Retornar ao Menu")

        opcao = input("Escolha uma opção")


        #Consultar todos
        if opcao == "1":
            for livro in lista_livros:
                print(f'Id: {livro['id']}')  
                print(f'Nome: {livro['nome']}')  
                print(f'Autor: {livro['autor']}')  
                print(f'Editora: {livro['editora']}')   

        #Consultar por Id
        elif opcao == '2':
            id_busca = int(input("Digite o ID do Livro: "))
            
            encontrado = False
            for livro in lista_livros:
                if livro["id"] == id_busca:
                    print(f'Id: {livro['id']}')
                    print(f'Nome: {livro['nome']}')  
                    print(f'Autor: {livro['autor']}')  
                    print(f'Editora: {livro['editora']}')
                    encontrado = True
            if not encontrado:
                print("Livro não encontrado")
        
        #Consultar por Autor 
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ")

            encontrado = False

            for livro in lista_livros: 
                if livro["autor"].lower() == autor_busca.lower():
                    print(f'Id: {livro['id']}')
                    print(f'Nome: {livro['nome']}')  
                    print(f'Autor: {livro['autor']}')  
                    print(f'Editora: {livro['editora']}')
                    encontrado = True
            if not encontrado:
                print("Autor não encontrado")

#Função remover livro
def remover_livro():
    while True:
        id_remover = int(input("Digite o Id do livro que deseja remover: "))
        encontrado = False
        for livro in lista_livros:
            if livro["id"] == id_remover:
                lista_livros.remove(livro)
                print(f'Livro removido com sucesso')
                encontrado = True
                return 
        if not encontrado:
            print('Id invalido')

#Programa Principal
print('Bem vindo ao Sistema de Gerenciamento de Livros')
print('Danielle Caricati')

while True:
    print("----Menu Principal----")
    print("1 - Cadastrar Livro")
    print("2- Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro(id_global)
        if_global +=1

    elif opcao == "2":
        consultar_livro()
    
    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        print("Programa encerrado.")
        break
    
    else:
        print("Opção Inválida")