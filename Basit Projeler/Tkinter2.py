import turtle

view = turtle.Screen()
view.bgcolor("white")
tosba = turtle.Turtle()
tosba.shape("triangle")
tosba.color( "black")

tosba.penup() #arkasında çizgi çizmesin 
size = 10
for i in range(100):
    tosba.stamp()   #basıp basıp çeksin
    size = size + 2
    tosba.forward(size)
    tosba.right(40)

view.mainloop()  #pencerenin açık kalmasını sağladık