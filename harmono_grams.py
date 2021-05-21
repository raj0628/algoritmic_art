import turtle
from math import pi, sin, e
import random
from harmonograph_generator import *
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Harmonographs")
pen.color("black")
name_list = ['Pattern 1', "Pattern 2", "Pattern 3"]
name = random.choice(name_list)
screen.setup(1000, 800)
# frequencies  and phase for graph :
f1, f2, f3, f4, p1, p2, p3, p4 = graph_selector(name)
# decay constants:
d1 = 0.005
d2 = 0.005
d3 = 0.005
d4 = 0.005

t = 0
dt = 0.02
turtle.clear()
pen.speed(10)
draw = True
pen.penup()
pen.setpos(-450, 320)
pen.write(name, font=('Lemon', 30, 'normal'))
pen.pendown()
pen.penup()
pen.setpos(0, 0)
pen.pensize(3)
re = 237
pl = 20
n = 50
width = 0
del_w = 0
def draw():
    global t
    x = 200 * sin(f1 * t + p1) * e ** (-t * d1) + 200 * sin(f2 * t + p2) * e ** (-t * d2)
    y = 200 * sin(f3 * t + p3) * e ** (-t * d3) + 200 * sin(f4 * t + p4) * e ** (-t * d4)
    pen.setpos(x, y)
    t += dt
while draw:
    pen.pendown()
    if re == 237:
        pl = -pl
    elif re == 57:
        pl = -pl
    re += pl
    if width == 12:
        del_w = -0.25
    if width == 0:
        del_w = 0.25
    width += del_w
    pen.pensize(width)
    for i in range(n):
        # for colour gradient
        pen.pencolor('#' + hex(re)[2:] + '00' + hex(255 - re)[2:])
    draw()
    if t > 40:
        pen.hideturtle()
        screen.exitonclick()
        draw = False
