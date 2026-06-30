#We have an index referring to each item in the list, and a second index referring to each character of the string.
backpack = ['Hammer', 'Knife', 'Water', 'Rope']
print(backpack[0][1]) #the 1º bracket access the index of the item, the 2º bracket access the character of the item
print(backpack[1][4])
print(backpack[2][0])

#To run a double index scan use two nested loops.
for item in backpack:#this loop will scan the index of each item in the list
    for char in item:#this loop will scan the index of each character in each item in the list
        print(char, end='')#the end='' lets it not jump the line for each character
    print() #empty print() makes it print in next line





