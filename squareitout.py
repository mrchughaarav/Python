import math

def square_filter(start, end):
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = math.pow(num, 2)  # Find square

        if int(square) % 2 == 0:
            even_squares.append(int(square))
        else:
            odd_squares.append(int(square))

    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

# Example
square_filter(1, 10)