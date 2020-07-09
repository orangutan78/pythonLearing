import turtle
import random
turtle.shape ("turtle")
turtle.setup(600,600)
turtle.speed(0)

for i in range(1,300):
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    turtle.goto(x,y)

turtle.exitonclick()
