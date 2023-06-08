import turtle

turtle.bgcolor("black")
kalem=turtle.Turtle()
kalem.speed(20)


for i in range(180):
    if (i%6==0):
        kalem.pencolor("yellow")
    if i%6==1:
        kalem.pencolor("red")
    if i%6==2:
        kalem.pencolor("gray")
    if (i%6==3):
        kalem.pencolor("green")
    if i%6==4:
        kalem.pencolor("white")
    if i%6==5:
        kalem.pencolor("purple")

    kalem.width(i//100+1)
    kalem.fd(i)
    kalem.left(59)

turtle.mainloop()
