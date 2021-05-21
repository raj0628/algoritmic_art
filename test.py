import turtle
from math import pi,sin,e
import random
pen=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(1000,800)
screen.title("Harmonographs")

pen.color("white")


#frequencies  and phase for graph :
f1,f2,f3,f4,p1,p2,p3,p4=2.04,1,2.04,1,0,0,pi/2,pi/2

#decay constants:
d1=0.002
d2=0.002
d3=0.002
d4=0.002

t=0
dt=0.05
turtle.clear()
pen.speed(10)
draw=True
re = 237
pl=20
n=50
boldness=1
del_b=0.1
del_width=1

def draw():
   global t
   x= 200 * sin(f1 * t + p1) * e ** (-t * d1) +200*sin(f2*t +p2)*e**(-t*d2)
   y= 200 * sin(f3 * t + p3) * e ** (-t * d3) +200*sin(f4*t +p4)*e**(-t*d4)
   pen.setpos(x,y)
   t += dt

while draw:
    draw()
    if re == 237:
        pl=-pl
    elif re == 57:
        pl=-pl
    re += pl
    pen.pensize(boldness)
    if boldness==10:
        del_b=-0.5
    if boldness==1:
        del_b=0.5
    boldness+=del_b
    for i in range(n):
        pen.pencolor('#'+hex(re)[2:]+'00'+hex(255-re)[2:])    #for colour gradient
    print(t)
    if t>300:

      pen.hideturtle()
      screen.exitonclick()
      draw=False