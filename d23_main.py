import time
from turtle import Screen
from d23_player import Player
from d23_car_manager import CarManager
from d23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
