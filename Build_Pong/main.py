from paddle import CreatePaddle
from ball import CreateBall
from scoreboard import ScoreBoard
from screen_design import DesignScreen
import time
import collisions

WINNING_SCORE = 1
SLEEP = 0.05
DISTANCE_FROM_CENTER = 350

if __name__ == "__main__":

    # Create Screen
    screen = DesignScreen()

    # Create paddle on the left
    l_paddle = CreatePaddle(-DISTANCE_FROM_CENTER)

    # Create paddle on the right
    r_paddle = CreatePaddle(DISTANCE_FROM_CENTER)

    # create ball
    ball = CreateBall()

    # create Scoreboard
    scoreboard = ScoreBoard()

    # Set commands for paddles
    screen.commands(l_paddle, r_paddle)

    game_is_on = True

    while game_is_on:
        time.sleep(SLEEP)
        screen.screen_update()

        # Keeps ball moving
        ball.move_ball()

        # detect collision with wall
        collisions.wall_collision(ball)

        # detect collision with paddle
        collisions.paddle_collision(ball, l_paddle, r_paddle)

        # detect if ball hit past l_paddle
        collisions.l_paddle_collision(ball, scoreboard)

        # detect if ball hit past r_paddle
        collisions.r_paddle_collision(ball, scoreboard)

        # end game
        game_is_on = scoreboard.end_game(WINNING_SCORE, game_is_on)

    screen.exit_screen()
