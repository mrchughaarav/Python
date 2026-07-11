# Create a Dog class
class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

# Create two objects
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Display details of the first dog
print("Dog 1")
print("Animal:", Dog.animal)
print("Breed:", dog1.breed)
print("Colour:", dog1.colour)

print()

# Display details of the second dog
print("Dog 2")
print("Animal:", Dog.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)