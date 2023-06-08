"""
Aşağıdaki kod kader ağacı uygulamsıdır.
"""

import turtle
data = turtle.Turtle()
data.screen.bgcolor("white")
data.pensize(2)  # Kalem boyutu
data.color("brown")  # Kalem rengi
data.left(90)  # Sola dön
data.backward(100)  # Geri gel
data.speed(500)  # Hız
data.shape("turtle")  # Kalemin şekli; turtle, arrow, circle, square, triangler, classic

def kader_agaci(i):
    if i<10:
        return
    else:
        data.forward(i) # ileri git
        data.color("green")
        data.circle(2) # Yuvarlak yap
        data.color("brown")
        data.left(30)
        kader_agaci(3*i/4)
        data.right(60) # Sağa git
        kader_agaci(3*i/4)
        data.left(30)
        data.backward(i)
kader_agaci(100)
turtle.done()