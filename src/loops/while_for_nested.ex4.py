phrase = input('Enter a message: ')
size = len(phrase)

while ((size < 10) or (size > 30)):
    phrase = input('Enter a message')
    size = len(phrase)
print(f"With spaces: {phrase}")
print(f'Without space: ', end="")

for i in range (0, size, 1):
    if (phrase[i] != ''):
       print(phrase[i], end="")