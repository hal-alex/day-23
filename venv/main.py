# Turtle crossing the road game

#Steps:
# 1. Design player class - will create a turtle, "listen" to the "Up" key and move it to a certain point
# once "Up" is detected
# 2. Design car manager class - creates cars, moves them and speeds them up whenever a player progresses to the next level
# 3. Detect when any car hits the turtle
# 4. Design scoreboard class - will keep track of the user's progress and display the score


import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
carmanager = CarManager()
player = Player()
car_car = Car()
screen.onkeypress(player.move_up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_a_car()
    carmanager.move_all_cars()

    for car in carmanager.all_cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 280:
        player.turtle_reset()
        carmanager.next_level()
        scoreboard.increase_level()
