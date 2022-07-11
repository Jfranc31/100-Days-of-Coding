def wall_collision(ball):
    """
    Change direction of the y for the ball if it gets to the top or bottom of screen.
        parameter ball: The ball is a turtle that is being checked for if it hits top or bottom of screen.
    """
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


def paddle_collision(ball, l_paddle, r_paddle):
    """
    Check for if ball collided with the paddles, to then bounce back.
        parameter ball: The ball is a turtle that is being checked for its distance from both paddles, and
        from the walls.
        parameter l_paddle: A turtle that is being used to bounce the ball.
        parameter r_paddle: A turtle that is being used to bounce the ball.
    """
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


def l_paddle_collision(ball, scoreboard):
    """
    If the ball bounced on the left wall, point is given to the second player.
        parameter ball: The ball is a turtle that is being checked for its distance from the left wall.
        parameter scoreboard: Used to keep track of the points being added to the player.
    """
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.change_score(2)


def r_paddle_collision(ball, scoreboard):
    """
    If the ball bounced on the right wall, point is given to the first player.
        parameter ball: The ball is a turtle that is being checked for its distance from the right wall.
        parameter scoreboard: Used to keep track of the points being added to the player.
    """
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.change_score(1)
