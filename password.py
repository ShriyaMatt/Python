import random
import string

def generate_password(length=12):
    """
    Generate a random password containing lowercase, uppercase, and digits.
    The password is shuffled to ensure randomness.
    """
    if length < 3:
        raise ValueError("Password length must be at least 3 to include all character types.")

    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure at least one of each type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Fill the rest of the password length with random choices from all pools
    all_chars = lowercase + uppercase + digits
    password_chars += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)

    # Join list into a string
    return ''.join(password_chars)

# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (min 3): "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)