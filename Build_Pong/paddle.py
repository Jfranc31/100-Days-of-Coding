from turtle import Turtle
MOVE_SPACE = 40
ON_SCREEN = 230


class CreatePaddle(Turtle):
    def __init__(self, beginning_space: int):
        """
        Create paddle as a white square.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_coordinate = beginning_space
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle()

    def paddle(self):
        """
        Place the paddle at beginning position.
            parameter x_coordinate: value for x coordinate
        """
        self.goto(self.x_coordinate, 0)

    def up(self):
        """
        Move paddle up.
        """
        if self.ycor() < ON_SCREEN:
            self.sety(self.ycor() + MOVE_SPACE)

    def down(self):
        """
        Move paddle down.
        """
        if self.ycor() > -ON_SCREEN:
            self.sety(self.ycor() - MOVE_SPACE)
