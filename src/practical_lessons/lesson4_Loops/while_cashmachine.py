valor = int(input('Digite o valor que deseja sacar: R$ '))

while True:
    if valor >= 100: #notas
        cont100 = valor // 100 #calculo de cédulas 
        valor = valor - cont100 * 100 #retira as notas
        print(f'Cédulas de 100: {cont100}')
        if not valor: #Encerra o laço se não tiver mais dinheiro na variavel valor
            break
    
    elif valor >= 50: #notas
        cont50 =  valor // 50 #calculo de cédulas 
        valor = valor - cont50 * 50 #retira as notas
        print(f'Cédulas de 50: {cont50}')
        if not valor:
            break

    elif valor >= 20: #notas
        cont20 = valor // 20 #calculo de cédulas 
        valor = valor - cont20 * 20#retira as notas
        print(f'Cédulas de 20: {cont20}')
        if not valor:
            break

    elif valor >= 10: #notas
        cont10 = valor // 10 #calculo de cédulas 
        valor = valor - cont10 * 10 #retira as notas
        print(f'Cédulas de 10: {cont10}')
        if not valor:
            break

    elif valor >= 5: #notas
        cont5 = valor // 5 #calculo de cédulas 
        valor = valor - cont5 * 5 #retira as notas
        print(f'Cédulas de 5: {cont5}')
        if not valor:
            break
    
    if valor: #notas
        cont1 = valor 
        print(f'Cédulas de 1: {cont1}')
        break