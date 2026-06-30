preco = int(input('Digite o valor do produto: '))
percentual = int(input('Digite o percentual de desconto: '))

desconto = preco * (percentual / 100)
total = preco - desconto

print(total)