import turtle

turtle.speed(500)
turtle.bgcolor("black")

for i in range(15):
    for color in ("red", "magenta", "blue", "cyan", "green", "white", "brown", "orange", "silver"):
        turtle.color(color)
        turtle.pensize(3)
        turtle.left(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)