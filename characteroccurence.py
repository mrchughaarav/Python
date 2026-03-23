string = input("Enter your own word: ")
char = input("Enter your own Character: ")
i = 0
count = 0
while (i < len(string)):

     if(string[i] == char):
          count = count+1
     i = i+1

print("The total number if times", char, "was displayed is", count)