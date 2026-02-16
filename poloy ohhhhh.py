class BMW:
    def fuel_type(self):
        """Display the fuel type for BMW"""
        print("BMW uses Petrol or Diesel.")

    def max_speed(self):
        """Display the max speed for BMW"""
        print("BMW max speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        """Display the fuel type for Ferrari"""
        print("Ferrari uses Petrol.")

    def max_speed(self):
        """Display the max speed for Ferrari"""
        print("Ferrari max speed: 340 km/h")


# Function to demonstrate polymorphism
def car_details(car):
    """Call the same methods on different car objects"""
    car.fuel_type()
    car.max_speed()
    print("-" * 30)


# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Using polymorphism: same function works for different objects
for vehicle in (bmw_car, ferrari_car):
    car_details(vehicle)