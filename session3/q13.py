'''
Take a number as input. Using the ternary operator, print "Even"or"Odd" in a single line.
'''

number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)