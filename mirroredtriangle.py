import turtle

# Setup
t = turtle.Turtle()
t.speed(3)

# Function to draw a right-angled triangle
def draw_triangle():
    t.forward(100)     # base
    t.left(90)
    t.forward(100)     # height
    t.left(135)
    t.forward(141)     # hypotenuse

# Draw first triangle
draw_triangle()

# Move to position for mirrored triangle
t.penup()
t.goto(0, 0)
t.pendown()

# Flip direction for mirror
t.setheading(180)

# Draw mirrored triangle
draw_triangle()

# Finish
turtle.done()