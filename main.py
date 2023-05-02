from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
car = Car()
scoreboard = Scoreboard()


screen.screensize(500, 500)
screen.colormode(255)
screen.title("Turtle Crossing Game")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move, "Up")


game_on = True
while game_on:
    time.sleep(0.08)
    screen.update()
    car.move()
    car.create_car()

    if player.ycor() >= 305:
        player.reset_position()
        scoreboard.SCORE += 1
        scoreboard.update_score()
        car.SPEED *= 1.3

    for vehicle in car.cars:
        if vehicle.xcor() <= -400:
            car.cars.remove(vehicle)

    for vehicle in car.cars:
        if player.distance(vehicle) <= 15:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
