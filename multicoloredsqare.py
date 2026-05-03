import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

# Colours
colors = ["blue", "red", "orange"]

# Square settings
square_size = 180
section_width = square_size / 3

t.penup()
t.goto(-square_size/2, square_size/2)  # top-left corner
t.pendown()

# Draw 3 filled sections
for i in range(3):
    screen.bgcolor(colors[i])   # change background
    t.fillcolor(colors[i])
    t.begin_fill()
    
    for _ in range(2):
        t.forward(section_width)
        t.right(90)
        t.forward(square_size)
        t.right(90)
    
    t.end_fill()
    
    t.forward(section_width)  # move to next section
    time.sleep(1)  # pause so you can see background change

turtle.done()