def get_age():
    try:
        age_input = input("Enter your age: ").strip()

        # Check if input is a number
        if not age_input.isdigit():
            raise ValueError("Age must be a positive whole number.")

        age = int(age_input)

        # Check for realistic age range
        if age <= 0 or age > 150:
            raise ValueError("Please enter a realistic age between 1 and 150.")

        return age

    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def check_even_odd(age):
    if age % 2 == 0:
        print(f"Your age ({age}) is EVEN.")
    else:
        print(f"Your age ({age}) is ODD.")


# Main program
age = get_age()
if age is not None:
    check_even_odd(age)