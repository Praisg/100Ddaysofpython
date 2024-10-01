from turtle import Turtle, Screen

pride = Turtle()
myScreen = Screen()

#drawing a dashed line
for _ in range(4):
    pride.forward(10)
    pride.penup()
    pride.forward(10)
    pride.pendown()
myScreen.exitonclick()