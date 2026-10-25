'''
Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message.
'''
age = int(input("Enter the person's age: "))
has_valid_id = input("Do they have a valid ID? (True/False): ").lower() == "true"

if age >= 18 and has_valid_id:
    print("They can enter the venue.")
else:
    print("They cannot enter the venue.")