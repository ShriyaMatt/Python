# Define the Dog class
class Dog:
    # Class variable (shared by all instances)
    animal = "Dog"

    # Constructor to initialize breed and colour
    def __init__(self, breed, colour):
        # Input validation
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Breed must be a non-empty string.")
        if not isinstance(colour, str) or not colour.strip():
            raise ValueError("Colour must be a non-empty string.")

        self.breed = breed.strip().title()
        self.colour = colour.strip().title()

    # Method to display dog details
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print("-" * 30)


# Create two Dog objects with different breeds and colours
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Display details of both dogs
dog1.display_details()
dog2.display_details()