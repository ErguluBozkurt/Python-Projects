"""
Aşağıdaki kod enkli altıgen şekil çizimi yapar.
"""

import turtle

window = turtle.Screen()
pen = turtle.Turtle()
pen.color("red", "brown")
pen.pensize(10)
pen.speed(1)
pen.begin_fill()

for i in range(6):
    if(i== 0):
        pen.pencolor("silver")
    if(i== 1):
        pen.pencolor("yellow")
    if(i== 2):
        pen.pencolor("brown")
    if(i== 3):
        pen.pencolor("black")
    if(i== 4):
        pen.pencolor("green")
    if(i== 5):
        pen.pencolor("red")
    pen.fd(200)
    pen.left(60)
pen.end_fill()
window.mainloop()