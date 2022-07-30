from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 40, "normal")
START_BALL = (0, 250)


class ScoreBoard(Turtle):
    def __init__(self):
        """
        Create scoreboard of both players points.
        """
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(START_BALL)
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Track score and show it on the screen.
        """
        self.write(arg=f"{self.score1}   {self.score2}", align=ALIGN, font=FONT)

    def change_score(self, player: int):
        """
        Increases score for player who scored.
            parameter player: int value to pick which player's score increases.
        """
        if player not in [1, 2]:
            raise ValueError

        if player == 2:
            self.score2 += 1
        else:
            self.score1 += 1

        self.goto(START_BALL)
        self.clear()
        self.update_scoreboard()

    def end_game(self, winning_score, game_is_on):
        """
        Checking if game has ended when either player has the winning amount of points.
            parameter scoreboard: Used to keep track of the points players have.
            parameter winning_score: The amount needed for either player to win the game.
            parameter game_is_on: Boolean stating if the game has ended or continues.
        """
        if self.score1 == winning_score or self.score2 == winning_score:
            game_is_on = False
            self.game_over(winning_score)
        return game_is_on

    def game_over(self, winning_point: int):
        """
        Stops program and shows the winner.
            parameter winning_point: Number of points needed to win.
        """
        winner = 0
        if self.score1 == winning_point:
            winner = 1
        elif self.score2 == winning_point:
            winner = 2
        self.goto(0, 0)
        self.write(arg=f"Game Over, Winner is Player {winner}", align=ALIGN, font=FONT)
