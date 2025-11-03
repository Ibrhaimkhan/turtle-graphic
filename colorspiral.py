# colorspiral.py
"""A module for drawing colorful spirals of up to 6 sides"""
import turtle
def cspiral(sides=12, size=360, x=0, y=0):
    """Draws a colorful spiral on a black background.
    Arguments:
    sides -- the number of sides in the spiral (default 6)
    size -- the length of the last side (default 360)
    x, y -- the location of the spiral, from the center of the screen
    """
    t=turtle.Pen()
    t.speed(0)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    turtle.bgcolor("black")
    colors=["red", "yellow", "blue", "orange", "green", "purple", "pink", "cyan", "magenta", "lime", "brown", "gray"]
    for n in range(0, size, 1):
        t.pencolor(colors[n % sides])
        t.forward(n * 3 / sides + n)
        t.left(360 / sides + 1)
        t.width(n * sides / 100)
        writeToTerminal(f"Drawing side {n} and the color this time is {colors[n % sides]}")
        # writeToTerminal(f"Drawing side {n+1} with color {colors[n%sides]}")
        # writeToTerminal(f"Drawing side with color ")
        turtle.time.sleep(0.5)
def writeToTerminal(msgIbi):
    """Writes a message to the terminal"""
    print(msgIbi)
    print("mak added this code")
cspiral()
