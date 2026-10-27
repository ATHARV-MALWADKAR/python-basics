'''
Ask a number from the user, print the multiplication table upto 10
'''

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")