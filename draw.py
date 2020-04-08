import turtle
from turtle import *

from my_turtle import color


def drawSun():
    color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
        turtle.end_fill()
        done()
