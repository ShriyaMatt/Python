import math

class Circle:
    def __init__(self, radius):
        # Ensure radius is non-negative
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


# Main program
try:
    # Take radius input from the user
    radius_input = float(input("Enter the radius of the circle: "))
    
    # Create Circle object
    circle = Circle(radius_input)
    
    # Display results
    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")