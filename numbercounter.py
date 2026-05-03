# Ask the user to input a number
num = int(input("Enter a number: "))

# Make sure the number is positive
if num < 0:
    num = -num

# Special case: if number is 0, it has 1 digit
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num = num // 10   # Remove the last digit
        count += 1        # Increase digit count

print("Number of digits:", count)