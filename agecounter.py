age = input("Enter your age: ")

if age.isdigit():
    age = int(age)

    if age % 2 == 0:
        print("The age entered is Even.")
    else:
        print("The age entered is Odd.")
else:
    print("Value Error: Please enter a valid integer age.")