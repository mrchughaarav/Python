# 1. Create lists of odd and even numbers under the user's input
num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]
even_numbers = [x for x in range(num) if x % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# 2. Create a list of fruits and capitalize the first letter of each
fruits = ["apple", "banana", "orange", "grape", "mango"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", updated_fruits)