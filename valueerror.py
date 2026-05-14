try:     #using a try and except
    number = int(input("Enter a number:  "))
    print("The number entered is", number)

except ValueError as ex:
    print("Exception:", ex)