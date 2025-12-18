import math

def circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter radius: "))
print("Circumference:", circumference(r))