# Operator Precedence
'''
** has the highest precedence, followed by *, /, //, %, +, and -.
and first need to solve the brackets if any, then the ** operator, then the *, /, //, and % operators, and finally the + and - operators.

** Exponentiation (raise to the power)-> Highest Precedence

* Multiplication        ->
/ Division              ->              Medium Precedence
// Floor Division       ->
% Modulus (remainder)   ->

+ Addition              ->              Lowest Precedence
- Subtraction           ->

'''

print(2 + 3 * 5)  # 2 + (3*5) = 17
print(2/3 + 5)  # (2/3) + 5 = 5.666666666666667
print(2 + 3 * 5**2)  # 2 + (3*(5**2)) = 77

#give the brackets to force to do which ever operation first
print((2 + 3) * 5)  # (2+3)*5 = 25
print(2/(3 + 5))  # 2/(3+5) = 0.25
print((2 + 3) * 5**2)  # (2+3)*(5**2) = 125