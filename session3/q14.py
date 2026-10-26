'''
A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
'''

purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount > 5000:
    discount = 0.20 * purchase_amount
elif purchase_amount > 2000:
    discount = 0.10 * purchase_amount
elif purchase_amount > 1000:
    discount = 0.05 * purchase_amount
else:
    discount = 0

print("The discount is:", discount)
print("The final amount to be paid is:", purchase_amount - discount)