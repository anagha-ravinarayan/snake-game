from turtle import Turtle

from constants import SCORE_BOARD_POS_X, SCORE_BOARD_POS_Y, ALIGNMENT, SCORE_FONT, GAME_OVER_FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_properties()
        self.display_score()

    def set_properties(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(SCORE_BOARD_POS_X, SCORE_BOARD_POS_Y)

    def display_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def increment_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

