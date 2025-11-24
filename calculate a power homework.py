# Simple program to calculate power using a for loop

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1
for _ in range(exponent):
    result *= base

print(f"{base} raised to the power {exponent} is {result}")