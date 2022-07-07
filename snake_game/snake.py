from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
        Setting the beginning segments of the snake, making the snake, keeping track of the head of the snake.
        """
        self.segments = []
        self.snake()
        self.head = self.segments[0]

    def snake(self):
        """
        Setting 3 segments to be a white square one after the other to be the snake.
        """
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """
        Setting the last segment of the snake to go to the next segments place, while also moving the head of the
        snake continuously forward so that no matter the direction, the segments will follow.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Moving the snake upwards as long as it is not facing downwards.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Moving the snake downwards as long as it is not facing upwards.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Moving the snake left as long as it is not facing right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Moving the snake right as long as it is not facing left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
