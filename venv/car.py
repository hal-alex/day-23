from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        
        random_color = random.choice(COLORS)
        self.color(random_color)

        random_y_pos = random.randint(-250, 250)
        self.goto(x = 300, y = random_y_pos)
