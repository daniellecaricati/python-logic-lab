supermarket = ['Bread', 'Cake', 'Milk', 'Biscuit', 'Rice']
#another way to scan a double index
for i in range (0, len(supermarket), 1): #this loop scans the items 
    for j in range(0, len(supermarket[i]),1): #this loop scans the character of items
        print(supermarket[i][j], end= '') #asking to print both scans
    print()