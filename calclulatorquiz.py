def addition(a,b):
    return (a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return(a*b)
def division(a,b):
    return(a/b)

try:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation you would like to use (+,-,*,/)")
    if operation == "+":
        print("The result is", addition(num1,num2))
    elif operation == "-":
        print("The result is", subtraction(num1,num2))
    elif operation == "*":
        print("The result is", multiplication(num1,num2))
    elif operation == "/":
        print("The result is", division(num1,num2))
    else:
        print("Please enter a valid operation.")

except ZeroDivisionError:
    print("The number cannot be divided by 0!")
except ValueError:
    print("Enter a  valid number!")