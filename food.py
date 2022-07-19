from turtle import Turtle
import random

from constants import POSITION_LOWER_BOUNDARY, POSITION_UPPER_BOUNDARY


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.set_properties()
        self.set_random_position()

    def set_properties(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("GreenYellow")
        self.speed("fastest")

    def set_random_position(self):
        x = random.randint(POSITION_LOWER_BOUNDARY, POSITION_UPPER_BOUNDARY)
        y = random.randint(POSITION_LOWER_BOUNDARY, POSITION_UPPER_BOUNDARY)
        self.setpos(x, y)
