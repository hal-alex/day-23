import random
from turtle import Turtle
from car import Car
from random import randint

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars_list = []
        self.speed_of_car = STARTING_MOVE_DISTANCE

    def create_a_car(self):
        random_number = random.randint(1, 10)
        if random_number <=5:
            car = Car()
            self.all_cars_list.append(car)

    def move_all_cars(self):
        for car in self.all_cars_list:
            car.backward(self.speed_of_car)

    def next_level(self):
        self.speed_of_car += MOVE_INCREMENT
