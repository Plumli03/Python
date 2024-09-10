import turtle
import color模組  # Assuming color模組 contains the circle function you provided

# Set up the turtle screen
視窗寬度 = 1400
視窗高度 = 700

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=視窗寬度, height=視窗高度, startx=50, starty=50)
wn.colormode(255)
wn.tracer(0)  # Turn off animation

skk = turtle.Turtle()
skk.shape('turtle')
skk.hideturtle()
skk.speed(0)

半徑r = 100
dx = 0.3 ; dy = 0.3
x = -視窗寬度 / 2+半徑r
y = 視窗高度 / 2-半徑r

while True:
    skk.clear()
    color模組.circle(skk, x, y, 半徑r, "plum")

    # Check boundaries for x-coordinate
    if x > 視窗寬度 / 2-半徑r or x < -視窗寬度 / 2+半徑r :
        dx = -dx
    x += dx

    #Check boundaries for y-coordinate
    if y > 視窗高度 / 2-半徑r or y < -視窗高度 / 2+半徑r :
        dy = -dy
    y += dy

    wn.update()  # Update the turtle screen

wn.mainloop()

