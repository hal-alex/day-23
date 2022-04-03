from turtle import Turtle
from car import Car

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.all_cars_list = []

    def create_a_car(self):
        car = Car()
        self.all_cars_list.append(car)

    def move_all_cars(self):
        for car in self.all_cars_list:
            car.backward(STARTING_MOVE_DISTANCE)
