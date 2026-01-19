test_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}

# Value to check frequency for
value_to_check = 1

# Count frequency using list comprehension
frequency = list(test_dict.values()).count(value_to_check)

print(f"The value {value_to_check} appears {frequency} time(s) in the dictionary.")