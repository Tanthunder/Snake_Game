import imp
from turtle import Turtle

START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    
    def create_snake(self):
        for i in START_POSITION:
            self.add_segment(i)

    def add_segment(self,pos):
            seg= Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for se in range(len(self.segments)-1,0,-1):
            new_x= self.segments[se-1].xcor()
            new_y= self.segments[se-1].ycor()
            self.segments[se].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)

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
