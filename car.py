from turtle import Turtle
import random


class Car:

    SPEED = 9

    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        for _ in range(1):
            self.add_car()

    def add_car(self):
        random_num = random.randint(1, 3)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.5, stretch_len=1.5)
            new_car.color(self.random_color())
            new_car.penup()
            new_car.goto(x=400, y=self.random_y())
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.SPEED)

    def speed(self):
        return random.randint(1, 10)

    def random_y(self):
        return random.randrange(-250, 250, 75)

    def random_color(self):
        colors = ["red", "blue", "green", "yellow", "black", "orange", "pink"]
        return random.choice(colors)

