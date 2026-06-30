print('Integers from 3 to 12, including 12')

x = 3
while (x < 13):
    print(x)
    x = x + 1

print('-' * 20)

for i in range(3, 13, 1):
    print(i)

print('-' * 20)
print('Integers from 0 to 9, every 2, except 9')

x = 0
while (x < 9):
    print(x)
    x += 2

print('-' * 20)

for i in range(0, 9, 2):
    print(i)
