from turtle import Turtle, Screen
import random

pride = Turtle()
colors =["CornflowerBlue", "DarkOrchid","IndianRed","DeepSkyBlue","wheat","SlateGray","SeaGreen"]

num = 3
while num <= 8: #Printing a triangle up to a decagon
    for _ in range(num):
        pride.forward(100)
        pride.right(360/num)
    num += 1
    pride.color(random.choice(colors)) 
    
myScreen = Screen()
myScreen.exitonclick()