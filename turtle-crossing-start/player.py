from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """
        The amount the turtle moves up forward.
        """
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        """
        If turtle makes it to the end, gets sent back to the beginning for next level.
            return finish (Boolean): True if next level, False if same level.
        """
        finish = False
        if self.ycor() == FINISH_LINE_Y or self.ycor() > FINISH_LINE_Y:
            finish = True
            self.goto(STARTING_POSITION)
        return finish
