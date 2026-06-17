# Decimal to Binary Converter

decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Removes the '0b' prefix

print("Binary equivalent:", binary)