# Step 1: Create the Parent Class
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    # Step 2: Parent Method
    def show_details(self):
        print("Brand:", self.brand)
        print("Maximum Speed:", self.max_speed, "km/h")


# Step 3: Create the Child Class
class Car(Vehicle):

    # Step 4: Child Constructor
    def __init__(self, brand, max_speed, model, seats):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats

    # Step 5: Override Parent Method
    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    # Step 6: Child-Only Method
    def fuel_type(self):
        print("Fuel Type: Petrol")


# Step 7: Create and Test the Object
my_car = Car("Toyota", 220, "Corolla", 5)

print("Car Details:")
my_car.show_details()

print()
my_car.fuel_type()

print()

# Step 8: Check Inheritance
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))