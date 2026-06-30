a = int(input('Digite o 1° lado :'))
b = int(input('Digite o 2° lado :'))
c= int(input('Digite o 3° lado :'))

if ((a > 0 and b > 0 and c > 0) and (a + b > c or a + c > b or b + c > a)):
    if (a != b and a != c and b != c): 
        print ('Triangulo escaleno!') #tres lados diferentes
    else:
        if (a == b and b == c):
            print('Triangulo equilatero!')#todos os lados iguais
        else:
            ('Triangulo isosceles!')
else:
    print ('Ao menos um dos valores indicados não serve para formar um triangulo')