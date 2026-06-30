#Criando list 
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)

#Conta quantas vezes o numero 7 aparece na lista
print(notas.count(7))

#Alterar o ultimo valor da lista
notas[-1] = 4
print(notas)

#Achar o maior numero
print(max(notas))

#Ordenar a lista 
notas.sort()
print(notas)

#Média das notas da lista - sum() soma total , len() pega o tamanho total 
print(sum(notas) / len(notas))