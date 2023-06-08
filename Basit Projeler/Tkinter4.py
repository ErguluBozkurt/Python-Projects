"""
Kalp tasarımı yapar.
"""

import math 
import turtle


data = turtle.Turtle()
def ask(data):
    return(16*math.sin(data)**3)
def sevgi(data):
    return(13*math.cos(data)-5*\
        math.cos(2*data)-2*\
            math.cos(3*data)-\
                math.cos(4*data))
    

data.speed(500)
turtle.bgcolor("black")

for i in range(2550):
    
    data.goto((ask(i)*20, sevgi(i)*20))
    data.pencolor("red")
    data.goto(0,0)
    
    
	
	