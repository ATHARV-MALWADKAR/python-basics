'''
Sum of all the numbers from 1 to 100 divisible by 2 and 7
'''
total = 0
for i in range(1, 101):
    if i % 2 == 0 and i % 7 == 0:
        total += i
print(total)