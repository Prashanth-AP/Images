from turtle import Screen
import time
from player import Player
from car_manager import CarManager
screen=Screen()

screen.tracer(0)
screen.setup(width=600,height=600)
player=Player()
car_manager=CarManager()
screen.listen()
screen.onkey( player.go_up,"Up")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager=create_car(new_car)
    car_manager.move_cars()

    for car in car_manager_.all cars:
        if car.distance(payer)<20:
            game_is_on=False
screen.exitonclick()

