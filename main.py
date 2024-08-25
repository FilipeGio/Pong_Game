from paddle import Paddle
from score import Score
from turtle import Screen
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor('black')
screen.tracer(0)

left_wall = (screen.window_width() - screen.window_width() * 1.5) + 20
right_wall = screen.window_width() / 2 - 20
top_wall = screen.window_height() / 2
bottom_wall = screen.window_height() - screen.window_height() * 1.5



player1 = Paddle((left_wall, 0))
player2 = Paddle((right_wall, 0))
score1 = Score((-20, top_wall - 30))
score2 = Score((20, top_wall - 30))
score1.center_line()
ball = Ball()
gols_player1 = 0
gols_player2 = 0

screen.listen()
screen.onkeypress(key='w', fun=player1.up_move)
screen.onkeypress(key='s', fun=player1.down_move)

while True:
    screen.update()
    ball.forward(.2)

    # Detect collision with wall
    if ball.ycor() < bottom_wall or ball.ycor() > top_wall:
        ball.wall_hit()

    # Detect collision with pad
    if ball.distance(player1.new_pad) < 15:
        ball.move_right()
    elif ball.distance(player2.new_pad) < 15:
        ball.move_left()

    # Detect collision with player 2
    if ball.ycor() > player2.new_pad.ycor():
        player2.up_move()
    else:
        player2.down_move()

    # Score count
    if ball.xcor() < -280:
        gols_player2 += 1
        score2.score_count(gols_player2)
        ball.goto(0, 0)
        player1.new_pad.goto(-280, 0)
        sleep(1)
    elif ball.xcor() > 280:
        gols_player1 += 1
        score2.score_count(gols_player1)
        ball.goto(0, 0)
        player1.new_pad.goto(-280, 0)
        sleep(1)

