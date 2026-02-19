# Finding the  marks
maths = int(input("maths: " ))
english = int(input("english: " ))
science = int(input("science: " ))
hindi = int(input("hindi: " ))

# Calculating the total marks
sum = maths+english+science+hindi
print(f"The sum is {sum}")

perc = sum/400*100
print(end="Percantage mark = ")
print (perc)