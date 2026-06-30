#criar a função que checa os dados
def checagem_tipo(dado):
    match dado:
        case str(dado):
            print("String: ", dado)
        case int(dado):
            print('Inteiro: ', dado)
        case float(dado):
            print("Float: ", dado)
        case bool(dado):
            print("Boolean: ", dado)
        case _:
            print("Tipo desconhecido")

#lista com dados variados
dados = ['Python', 42, 3.14, 23, 'C', True, 0]

#percorre os itens da lista
for dado in dados:
    checagem_tipo(dado) #chama a função para cada item percorrido