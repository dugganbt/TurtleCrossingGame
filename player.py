STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color = 'black'
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def crossed_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def return_to_start(self):
        self.goto(STARTING_POSITION)


