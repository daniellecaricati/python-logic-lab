h_start = int(input('What time do you want to start?'))
h_finish = int(input('What time do you want to finish?'))

while ((h_start > h_finish) or (h_start < 0) or (h_start > 23) or (h_finish < 0) or (h_finish > 23)):
    h_start = int(input('What time do you want to start?'))
    h_finish = int(input('What time do you want to finish?'))

for h in range (h_start, h_finish + 1, 1):
    for m in range (0, 60, 1):
        for s in range (0, 60, 1):
            print(h,':', m, ':', s, 'h')