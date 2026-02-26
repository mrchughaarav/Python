height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height/100) **2
print(f"Your BMI is {bmi}")

if bmi <= 18.4:
    print("You are underweight.")
elif bmi<= 24.4:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.4:
    print("You are severely overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")