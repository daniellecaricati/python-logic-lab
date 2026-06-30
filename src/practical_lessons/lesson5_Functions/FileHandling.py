#Função para validar valor min e max.
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Função para ver se arquivo existe
def existeArquivo(nomeArquivo):
    try: #realizar tentativa
        a = open(nomeArquivo, 'rt') #open() abre o arquivo , rt - leitura
        a.close() #Semppre que abrir um arquivo, deve também fecha-lo
    except FileNotFoundError:
        return False
    else:
        return True


#Função para criar o arquivo
def criarArquivo(nomeArquivo):
    try: #realizar tentativa
        a = open(nomeArquivo, 'wt+') #open() abre o arquivo , wt - escrita, + atualizar leitura e escrita
        a.close() #Semppre que abrir um arquivo, deve também fecha-lo
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


#Função para cadastrar jogo
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at') #at - abre para escrita com conteudo que ja tem nele
    except:
        print('Erro ao abrir o arquivo')
    else:
        #O que vai dentro do arquivo
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close() #fechar o arquivo

#Função para listar arquivos
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


#Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
     print('Arquivo localizado!')
else: 
     print('Arquivo inexistente.')
     criarArquivo(arquivo)

while True:
    print('---MENU---')
    print('1 - Cadastrar item')
    print('2 - Listar Cadastros')
    print('3 - Sair')

    #validar dados para que usuario digite o que queremos
    op = valida_int('Escolha a opção desejada: ', 1, 3)

    if (op == 1):
        print('Opção cadastrar selecionada')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame) #chama a função cadastrarJogo

    elif (op == 2):
        print('Lista selecionada.')
        listarArquivo(arquivo)


    elif (op == 3):
        print('Sair')
        break
    