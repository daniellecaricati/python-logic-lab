km = int(input("Quantos km foram percorridos? "))
dias = int(input("Quantos dias o carro foi alugado?"))

valor = km * 0.15 + dias * 60
print (f'Km = {km}. Dias = {dias}.')
print (f'O valor total a pagar é R$ {valor}')