from turtle import Turtle, Screen
import random
from turtle import colormode



pride = Turtle()
colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

direction = [0, 90, 180, 270]
pride.pensize(15)
pride.speed("fastest")

for i in range(200):
    pride.forward(30)
    pride.color(randomColor())
    pride.setheading(random.choice(direction))


myScreen = Screen()
myScreen.exitonclick()