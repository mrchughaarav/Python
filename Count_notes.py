# Taking the total amount as an input from the user
amount = int(input("Please enter the amount:"))

# Calculating the number of notes in different denominations
note_1  = amount//100
note_2  = (amount%100)//50
note_3  = ((amount%100)%50)//10

print(f"notes of 100 dollars: {note_1}")
print(f"notes of 50 dollars: {note_2}")
print(f"notes of 10 dollars: {note_3}")