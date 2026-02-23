actual_cost = float(input("Please enter the Actual Product Price:"))
sale_amount = float(input("Please enter the Sale Amount:"))

if sale_amount > actual_cost:
    amount = sale_amount - actual_cost
    print(f"The total profit is {amount}")
else:
    print("No profit earnt!")