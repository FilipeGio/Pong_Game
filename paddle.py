from turtle import Turtle

COLOR = 'white'
SHAPE = 'square'
MOVE = 10


class Paddle:

    def __init__(self, position):
        self.create_paddle(position)

    def create_paddle(self, position):
        self.new_pad = Turtle(SHAPE)
        self.new_pad.color(COLOR)
        self.new_pad.setheading(90)
        self.new_pad.penup()
        self.new_pad.goto(position)
        self.new_pad.shapesize(stretch_len=2, stretch_wid=0.3)

    def up_move(self):
        self.new_pad.forward(MOVE)

    def down_move(self):
        self.new_pad.backward(MOVE)




