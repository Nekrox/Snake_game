from turtle import Turtle

POSITION_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in POSITION_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.snake_segments.append(new_snake_part)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]


    def move(self):
        snake_length = len(self.snake_segments)
        for segment_num in range(snake_length - 1, 0, -1):
            new_x = self.snake_segments[segment_num - 1].xcor()
            new_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
