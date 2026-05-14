try:
    num1, num2 = eval(input("Enter 2 numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    ("Division by zero is an error!!")

except SyntaxError:
    print("Comma is missing, please try again.")

except:
    print("Wrong input.")

else:
    print("No Exceptions.")

finally:
    print("This is will execute no matter what.")   