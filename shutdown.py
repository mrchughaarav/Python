decision = input("Enter your decision on shutting down the system(Y/N): ")
if decision == "Y":
    print("System shutting down.")
elif decision == "N":
    print("Aborting shutting the system down.")
else:
    print("Please enter a valid decision.")