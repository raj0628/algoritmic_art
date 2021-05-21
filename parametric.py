import turtle
turtle.setpos(-10,20)
turtle.speed(0)
for x in range(200):
    turtle.forward(300)
    turtle.right(90.5)

turtle.penup()
turtle.goto(200,60)
turtle.pendown()
turtle.pencolor("orange")
for x in range(100):
    turtle.forward(200)
    turtle.left(120.5)

turtle.hideturtle()
