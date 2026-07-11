# Test dictionary
test_dict = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "Coding": 1
}

# Print the dictionary
print("Test Dictionary:")
print(test_dict)

# Ask the user for a key
word = input("Enter the word you want to check: ")

# Check if the key exists
if word in test_dict:
    print("Frequency:", test_dict[word])
else:
    print("The word is not in the dictionary.")