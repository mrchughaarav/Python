import random
import string

# Ask the user for the password length
length = int(input("Enter password length: "))

# Characters to choose from
characters = string.ascii_letters + string.digits

# Generate password
password = []
for i in range(length):
    password.append(random.choice(characters))

# Shuffle the password
random.shuffle(password)

# Convert list to string
password = "".join(password)

print("Generated Password:", password)