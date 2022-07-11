from turtle import Turtle
BALL_X_MOVE = 10
BALL_Y_MOVE = 10


class CreateBall(Turtle):
    def __init__(self):
        """
        Create ball as a white circle.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_X_MOVE
        self.y_move = BALL_Y_MOVE

    def move_ball(self):
        """
        Keeps ball in constant motion.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Change direction of the y for the ball.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Change direction of the x for the ball.
        """
        self.x_move *= -1

    def reset_position(self):
        """
        After each point, set the ball back to center and send it in opposite direction.
        """
        self.goto(0, 0)
        self.bounce_x()
