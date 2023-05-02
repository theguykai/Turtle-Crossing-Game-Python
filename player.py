from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setposition(x=0, y=-300)

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.goto(x=0, y=-300)