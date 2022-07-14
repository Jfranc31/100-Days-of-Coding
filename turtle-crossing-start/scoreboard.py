from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"
GAME_OVER_FONT = ("Courier", 50, "normal")
GAME_OVER_ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        """
        Initializes the scoreboard at the top of screen.
        """
        super().__init__()
        self.penup()
        self.color("black")
        self.num_of_level = 1
        self.hideturtle()
        self.goto(-280, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Writes out the score the player has at the time.
        """
        self.write(arg=f"Level: {self.num_of_level}", align=ALIGN, font=FONT)

    def game_over(self):
        """
        Writes out game over at center of screen.
        """
        self.goto(-20, 0)
        self.write(arg="Game Over", align=GAME_OVER_ALIGN, font=GAME_OVER_FONT)

    def change_score(self):
        """
        Updates score by 1 and reprints the score
        """
        self.num_of_level += 1
        self.goto(-280, 270)
        self.clear()
        self.update_scoreboard()
