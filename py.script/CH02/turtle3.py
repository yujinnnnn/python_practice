import turtle
import random

colors =["red","green","blue","orange","purple","pink","yellow"]

turtle.width(7)
length = 5
for _ in range(30):
    color = random.choice(colors)
    turtle.forward(length)
    turtle.right(135)
    turtle.color(color)
    length=length+5 