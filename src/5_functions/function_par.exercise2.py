
def counter (end, start = 0, step = 1):
    for i in range (start, end+1, step):
        print(f'{i}', end=' ')
    print('\n')

counter(20, 10, 2)
counter(12)