from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars_list = []

    def create_a_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)#
        random_color = random.choice(COLORS)
        self.color(random_color)
        random_y_pos = random.randint(-250, 250)
        self.goto(x = 300, y = random_y_pos)
        self.all_cars_list.append(self)

    def move_single_car(self):
        for car in self.all_cars_list:
            car.backward(STARTING_MOVE_DISTANCE)