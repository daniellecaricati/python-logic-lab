#Conversion of Celsius x Fahrenheit
C = float(input("Type a Celsius temperature: "))
F = (9 * C / 5) + 32
print("Celsius: %.1f. Fahrenheit: %.1f." % (C, F)) #Classic
print("Celsius: {}. Fahrenheit: {}.".format(C, F))
