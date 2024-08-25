from turtle import Turtle


class Score:

    def __init__(self, position=(0, 0)):
        self.score = Turtle()
        self.score.color('white')
        self.score.penup()
        self.score.goto(position)
        self.score.ht()
        self.score_count()

    def score_count(self, score=0):
        self.score.clear()
        self.score.write(score, font=('Arial', 20, 'normal'), align='center')

    def center_line(self):
        new_turtle = Turtle()
        new_turtle.color('white')
        new_turtle.ht()
        new_turtle.penup()
        new_turtle.goto(0, 220)
        new_turtle.setheading(270)
        for n in range(0, 20):
            new_turtle.forward(21)
            if n % 2 == 0:
                new_turtle.pendown()
            else:
                new_turtle.penup()



