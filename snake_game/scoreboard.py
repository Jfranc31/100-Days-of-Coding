from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initializes the scoreboard at the top of screen.
        """
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Writes out the score the player has at the time.
        """
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        """
        Writes out game over at center of screen.
        """
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)

    def change_score(self):
        """
        Updates score by 1 and reprints the score
        """
        self.score += 1
        self.goto(0, 280)
        self.clear()
        self.update_scoreboard()
