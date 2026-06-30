#Função para validar valor min e max.
def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            print(f'Digite um numero entre {min} e {max}.')
        except ValueError:
            print('Digite apenas numeros.')


#Função para ver se arquivo existe
def existeArquivo(nomeArquivo):
    try: #tenta abrir o arquivo
        a = open(nomeArquivo, 'rt') #open() abre o arquivo , rt (read text)- leitura
        a.close() #Sempre que abrir um arquivo, deve também fecha-lo
    except FileNotFoundError: #Se arquivo ao existir
        return False
    else:
        return True


#Função para criar o arquivo
def criarArquivo(nomeArquivo):
    try: #realizar tentativa
        a = open(nomeArquivo, 'wt+') #open() abre o arquivo , wt+ - escrita, leitura , se arquivo nao existir , ele é criado
        a.close() #Semppre que abrir um arquivo, deve também fecha-lo
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


#Função para cadastrar jogo
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        with open(nomeArquivo, 'at') as a: #open - abre arquivo, a- append (escreva no final), O with fecha o arquivo automaticamente
            a.write(f'{nomeJogo};{nomeVideogame}\n') #as a- arquivo nomeado a, .write - grava no arquivo . \n pula proxima linha
    except:
        print('Erro ao abrir o arquivo')


#Função para listar arquivos
def listarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt') as a: #open () - Abre para leitura
            print(a.read()) #.read() ler o arquivo
    except:
        print('Erro ao ler o arquivo.')


#Programa principal
arquivo = 'games.txt' #var contendo nome do arquivo
if existeArquivo(arquivo): #chama a função existeArquivo
     print('Arquivo localizado!') #se for true, mostra aarquivo localizado
else: 
     print('Arquivo inexistente.') #caso contrario arquivo inexistente,  e cria o arquivo
     criarArquivo(arquivo)

while True: #repete o menu, so termina quando encontrar - break
    print('---MENU---')
    print('1 - Cadastrar item')
    print('2 - Listar Cadastros')
    print('3 - Sair')

    #validar dados para que usuario digite o que queremos
    op = valida_int('Escolha a opção desejada: ', 1, 3) #executa função validação

    if (op == 1):
        print('Opção cadastrar selecionada')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame) #chama a função cadastrarJogo para gravar no arquivo

    elif (op == 2):
        print('Lista selecionada.')
        listarArquivo(arquivo) #mostra tudo que esta salvo


    elif (op == 3):
        print('Sair')
        break
    