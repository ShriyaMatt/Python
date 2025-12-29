import math

# Get user input
try:
    angle_deg = float(input("Enter angle in degrees: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit(1)

# Convert degrees to radians (math functions use radians)
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)

# Handle tangent carefully (avoid division by zero)
try:
    tan_val = math.tan(angle_rad)
except Exception as e:
    tan_val = None

# Display results
print(f"sin({angle_deg}°) = {sin_val}")
print(f"cos({angle_deg}°) = {cos_val}")
if abs(cos_val) < 1e-15:  # Very close to zero → tan undefined
    print(f"tan({angle_deg}°) is undefined")
else:
    print(f"tan({angle_deg}°) = {tan_val}")