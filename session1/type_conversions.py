#implicit type conversion
x = 5
y = 2.0
z = x + y

print(f"Value of z: {z}, Type of z: {type(z)}")

#explicit type conversion
a = 10
b = float(a)
c = int(b)

print(f"Value of a: {a}, Type of a: {type(a)}")
print(f"Value of b: {b}, Type of b: {type(b)}")
print(f"Value of c: {c}, Type of c: {type(c)}")