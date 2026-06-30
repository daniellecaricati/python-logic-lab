print("Hello World!")
print("------------------------------------")
print(2  + 3) #arithmetic operation
print("2 + 3")
print("2" + "3") #Concatenation of strings
print("------------------------------------")
print("Hello, " + "World") #Concatenation of strings with space
print("Hello," , "World") #Concatenation of strings without space
print("------------------------------------")
print("Mathematic Operations")
print(10 * (5 + 7) / 4)
print(2 + 3 * 3) # * Multiplication
print(4**2 / 3) # **Exponetiation
print((9**2 / 2) * 6 - 1)
print("------------------------------------")
print("Assignments")
discipline = "Algorithms and Programming Logics" #name of variable = (assignment) string"" or int/float
score = 8.5
print(discipline) #asking to print the variable
print(score)
print("Discipline:", discipline, "Score:", score) #Showing variables with strings 
print("------------------------------------")
universe = 42
print("The meaning of life is the number: ", universe)
print("------------------------------------")
print("Logic Variables - Boolean") #Comparison
a = 1
b = 5
answer = a == b # == a is equal to b ? stored in answer
print(answer)
answer = a != b #  != is different ?
print (answer)
print("------------------------------------")
score1 = 10
total = 10 >= 7
print (total)
print("------------------------------------")
print("Index")
phrase = "Hello, World" #Storing string in variables
print(phrase)
print(phrase[0]) #asking to print the letter stored in index 0 = "H"
print(phrase[2])
print("------------------------------------")
print("Advanced Manipulation of Strings")
s1 = "Programming Logic"
s1 = s1 + " and Algorithms" #Concatenating the variable s1 and adding a string to it 
print(s1)
s2 = "A" + "-" * 10 + "B" # Multiply - 10 times
print(s2)
print("------------------------------------")
s3 = "Programming Languages:"
s3 = s3 + "\nPython" + "-" * 5 + "C" + "-" * 5 + "Java" + "-" * 5 + "PHP" #\n next line
print(s3)
print("------------------------------------")
note = 8.5
note1 = "You got an %f in the Algorithm subject" % note # %f= float number. to print inside the string . needs to add % + variable name outside of string
print(note1)
note1 = "You got an %.2f in the Algorithm subject" % note # %.2f only 2 decimals
print (note1)
print("------------------------------------")
note2 = 10
subject = "Algorithms"
result = "You got %d in the %s subject" % (note2, subject) # %d or %i = integer numbers, %s = string
print(result)
print("------------------------------------")
print("Modern Composition") 
note3 = 7
subject = "Algorithms"
result = "You got {} in the subject {}".format(note3, subject) # {} and needs to add .format(variables)
print(result)
print("------------------------------------")
print("Composition with f-strings") 
note4 = 9
subject = "Logic"
result = f'You got {note4} in the subject {subject}' #f' at the beginning and insert the variable name inside {}
print(result)
print("------------------------------------")
food = "temaki"
birth = 1988
age = birth / 37
msg = f"My favourite food is {food} and I am {age} years old."
print(msg)
print("------------------------------------")
print("Slicing")
ex = "Programming Logic and Algorithms Course"
print (ex[0:6]) # [start:end] index of slicing, starts with 0
print(ex[24:34]) # from 24 to 34
print(ex[:10]) #from the beginnig, to the 10th 
print(ex[:]) # prints the whole phrase
print("------------------------------------")
print("Length")
ex1 = "Python Language"
size = len(ex1) #to store the length of the variable ex1 to the variable size
print(ex1)
print(size)
print("------------------------------------")
name = "Danielle Karen Mendes Caricati"
comparison = len(name) >= 15 #comparing the length of nome to 15
print(comparison)
print("------------------------------------")
print("Input Function")
ask = input("What is your age?")  #Input() asks user and inserts data to the variable ask , Input always returns a string
print(ask)
ask1 = input("What is your name?")
print(f"Hello {ask1}, you are {ask} years old, welcome to my system!")
print("------------------------------------")
print("Casting") 
note5 = float(input("What was your score in the Algorithm subject?")) #float(input()) - converts the input string to float
print(f"You got an {note5} score")
print("------------------------------------")
print("Execution flow")
x = 1
y = 1
z = x + y # z = 2
x = x + 2 # x = 3
y = y - 1 # y = 0
z = x + y # z = 3 
x = y + 1 # x = 1
y = x - 1 # y = 0
z = x + y # z = 1 + 0 = 1
print(z)
print("------------------------------------")
