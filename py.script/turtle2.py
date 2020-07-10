import turtle
import random

pSize = 10
r,g,b = 0.0,0.0,0.0
turtle.title("Sketch Conch with Turtle")
turtle.shape('turtle')
turtle.color('violet')
turtle.pensize(pSize)
turtle.goto(0,0)
turtle.shape('turtle')
for i in range (0,120,1):
    turtle.pencolor((r,g,b))
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.left(30)
    turtle.forward(i+5)
turtle.done()
