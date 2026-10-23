'''
Take two numbers as input. Without using *, calculate and print their product 
using += in a way that adds the first number to itself the second number of times.without using loops.
'''
def product(a, b):
    if b == 0:
        return 0
    if b < 0:
        return product(-a, -b)

    result = product(a, b - 1)
    result += a
    return result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Product of {num1} and {num2} is {product(num1, num2)}")