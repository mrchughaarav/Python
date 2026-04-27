print("Half Pyramid Pattern of Stars (*): ")
n = int(input("Enter the amount of rows: " ))
for i in range (n):
    for j in range (i):
        print("* ", end="")
    print()