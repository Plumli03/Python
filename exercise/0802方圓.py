import turtle
import random

w=600
h=600
a=6 #row
b=4 #col

# Setup the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle6663629")
wn.colormode(255)
wn.setup(w, h)
wn.tracer(0)

# Setup the turtle
skk = turtle.Turtle()
skk.shape('turtle')
skk.speed(0)
skk.hideturtle()

# Draw squares with random colors
for n in range(a):  # 0-4 共5個
    for i in range(b):
        r = random.randint(0, 255)  # loop內重複
        g = random.randint(0, 255) # \換行
        b = random.randint(0, 255)

        skk.color(r, g, b)  # Set the outline and fill color
        skk.fillcolor(r, g, b)
        skk.begin_fill()

        # Move to starting position for each square
        skk.penup()
        skk.goto(-182 + n * 118, 182 - i * 118)
        skk.setheading(90)
        skk.pendown()

        # Draw the square
        for _ in range(4): #_ is a common placeholder when the loop variable is not used.
            skk.forward(108)
            skk.left(90)

        skk.end_fill()

# Finish up
turtle.done()

# 圓形
# skk.penup()
# skk.goto(300-10*n,0)
# skk.setheading(90)
# skk.pendown()
#
# skk.fillcolor(r,g,b)
# skk.begin_fill()
# skk.circle(300-10*n)
# skk.end_fill()