def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def division(a,b):
    return(a,b)

print("Choose the operation you would like to use:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
choice = input("Enter your choice(1/2/3/4): ")

num1 = float(input("Enter the first number you would like to choose: "))
num2 = float(input("Enter the second number you would like to choose: "))

if choice == "1":
    result = (num1 + num2)
elif choice == "2":
    result = (num1 - num2)
elif choice == "3":
    result == (num1*num2)
elif choice == "4":
    result == (num1/num2)

print("The result is", result)

try:
    num1 and num2
    if result%0==0:
        raise ZeroDivisionError
except ValueError:
    print("This is not a number! ")