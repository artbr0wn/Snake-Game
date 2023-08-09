# Created a snake class -- to tidy up the code!

from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.starting_snake()
        self.head = self.segments[0]

    def starting_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle(shape='square')
        segment_1.color('white')
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)

    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000, y=1000)
        self.segments.clear()
        self.starting_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for seg_num in range(start=2, stop=0, step=-1): -- python doesn't allow for letters in range funct
        # this for loop basically moves from back to front in sequential order
        for seg_num in range(len(self.segments) - 1, 0,-1):  # len function to make sure it works when new seg are made
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        # calling the first segment in range to move the entire snake forward now
        self.head.forward(MOVE_DISTANCE)

# directional keybinds to move the snake
# if current heading as a method isnt heading in the reverse (turtle heading method)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)