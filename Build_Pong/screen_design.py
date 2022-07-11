from turtle import Screen, Turtle
DOT_SIZE = 10
NUM_OF_DOTS = 29
SPACE_BETWEEN_DOTS = 20


class DesignScreen:
    def __init__(self):
        self.screen = Screen()
        self.line = Turtle()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong Game")
        self.screen.listen()
        self.screen.tracer(0)
        self.draw_line()

    def commands(self, l_paddle, r_paddle):
        """
        Commands for movement of the paddles.
            parameter screen: The screen being used in turtle files to make use of movements for paddles.
            parameter l_paddle: The left paddle to assign it up and down commands.
            parameter r_paddle: The right paddle to assign it up and down commands.
        """
        self.screen.onkey(fun=l_paddle.up, key="w")
        self.screen.onkey(fun=l_paddle.down, key="s")
        self.screen.onkey(fun=r_paddle.up, key="Up")
        self.screen.onkey(fun=r_paddle.down, key="Down")

    def draw_line(self):
        """
        Draw a line across the top to bottom of screen at the center.
            parameter line: The turtle for making the line go from top to bottom at the center.
        """
        self.line.shape("square")
        self.line.color("white")
        self.line.penup()
        self.line.hideturtle()
        self.line.goto(0, 280)
        self.line.setheading(270)
        for dot in range(NUM_OF_DOTS):
            self.line.dot(DOT_SIZE)
            self.line.forward(SPACE_BETWEEN_DOTS)

    def screen_update(self):
        """
        Update the screen so everything being done in the back shows up automatically.
        """
        self.screen.update()

    def exit_screen(self):
        """
        Exit screen after clicking on it.
        """
        self.screen.exitonclick()
