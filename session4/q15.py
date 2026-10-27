'''
Print all the numbers which are divisible by 3 and 5, from 1 to 100
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)