'''
Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400
'''
input_year = int(input("Enter a year: "))
if input_year < 10000 and input_year > 999:
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                print(f"{input_year} is a leap year")
            else:
                print(f"{input_year} is not a leap year")
        else:
            print(f"{input_year} is a leap year")
    else:
        print(f"{input_year} is not a leap year") 