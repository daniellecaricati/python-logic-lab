#Ao criar uma função, deve-se criar a documentação dela (explicar o funcionamento) - Docstrings

def soma3(x= 0, y= 0, z= 0):
    """
    Retorna o somatório de ate 3 valores numericos.
    Todos os parametros sao opcionais.

    x: valor numerico
    y: valor numerico
    z: valor numerico

    """
    return x + y + z

#chamada da função 
print(soma3(3,2))

#chamada do interactive help 
help(soma3)