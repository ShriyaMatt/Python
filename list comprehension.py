# Program: List Comprehension Examples

# --- Part A: Odd and Even Numbers ---
try:
    # Take user input and validate
    limit = int(input("Enter a positive integer: "))
    if limit <= 0:
        raise ValueError("Number must be positive.")

    # List of odd numbers below the limit
    odd_numbers = [n for n in range(limit) if n % 2 != 0]

    # List of even numbers below the limit
    even_numbers = [n for n in range(limit) if n % 2 == 0]

    print(f"Odd numbers below {limit}: {odd_numbers}")
    print(f"Even numbers below {limit}: {even_numbers}")

except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

# --- Part B: Fruits with Capitalized First Letter ---
fruits = ["apple", "banana", "mango", "grape", "orange"]

# Capitalize first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("\nOriginal fruits list:", fruits)
print("Capitalized fruits list:", capitalized_fruits)