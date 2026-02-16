birthdays = {}

# Raj has 5 friends — take input for each
for i in range(5):
    name = input(f"Enter the name of friend {i+1}: ").strip()
    birthday = input(f"Enter {name}'s birthday (e.g., 12-05-2000): ").strip()
    birthdays[name] = birthday  # Store in dictionary

print("\n--- Friends' Birthdays ---")
for friend, bday in birthdays.items():
    print(f"{friend}: {bday}")