from turtle import Turtle

from constants import SEGMENT_START_POSITIONS, MOVE_STEPS, UP, DOWN, LEFT, RIGHT


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SEGMENT_START_POSITIONS:
            seg = self.create_segment(position)
            self.segments.append(seg)

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].setpos(new_x, new_y)
        self.get_head().forward(MOVE_STEPS)

    def increment_length(self):
        seg = self.create_segment(self.segments[-1].position())
        self.segments.append(seg)

    def has_collided_with_itself(self):
        for seg in self.segments[1:]:
            if self.get_head().distance(seg) < 10:
                return True
        return False

    def up(self):
        if self.get_head().heading() != DOWN:
            self.get_head().setheading(UP)

    def down(self):
        if self.get_head().heading() != UP:
            self.get_head().setheading(DOWN)

    def left(self):
        if self.get_head().heading() != RIGHT:
            self.get_head().setheading(LEFT)

    def right(self):
        if self.get_head().heading() != LEFT:
            self.get_head().setheading(RIGHT)

    def get_head(self):
        return self.head

    @staticmethod
    def create_segment(position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.setpos(position)
        return seg
