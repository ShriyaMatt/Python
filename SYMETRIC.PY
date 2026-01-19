# Simple Python program to find symmetric difference between two sets

# Define two example sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Calculate symmetric difference
# Method 1: Using symmetric_difference() method
sym_diff = set1.symmetric_difference(set2)

# Method 2: Using ^ operator (alternative)
# sym_diff = set1 ^ set2

# Display the result
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", sym_diff)