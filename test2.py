import turtle
import random
from turtle import Screen

#turtle.tracer (False)

slot = turtle.Turtle()
#slot.speed(0)
turtle.setundobuffer(500)


for i in range(10):
    slot.forward(20)
    slot.left(10)
    slot.forward(20)

for i in range(10):
    slot.undo()




turtle.exitonclick()


