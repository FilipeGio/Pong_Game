from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

    def move_right(self):
        move = [randint(-20, 21), randint(340, 360)]
        self.setheading(choice(move))

    def move_left(self):
        self.setheading(randint(160, 201))

    def wall_hit(self):
        if 160 <= self.heading() <= 201:
            if self.heading() > 180:
                self.setheading(160)
            else:
                self.setheading(200)
        else:
            if self.heading() > 340:
                self.setheading(20)
            else:
                self.setheading(340)

