n = int(input("Enter a non-negative decimal number: "))


b = "" if n != 0 else "0"  # Handle zero case
while n > 0:               # Outer loop: process each bit
    for _ in range(1):     # Inner loop: prepend bit
        b = str(n % 2) + b
    n //= 2

print("Binary:", b)