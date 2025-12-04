# Get user input
num = int(input("Enter an integer: "))
    
# Handle negative numbers by taking absolute value
n = abs(num)
    
# Special case: if number is 0, it has 1 digit
if n == 0:
        count = 1
else:
        count = 0
        while n > 0:
            n //= 10  # Remove the last digit
            count += 1
    
print(f"Total digits in {num} = {count}")

