'''
Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both are equal.")