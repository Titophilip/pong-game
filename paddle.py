from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1.0, stretch_len=5.0, outline=None)
        self.color("white")
        self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

    def up(self):
        if self.ycor() <= 245:
            self.forward(20)

    def down(self):
        if self.ycor() >= -230:
            self.backward(20)

    def paddle_reset(self):
        self.goto(self.x, self.y)
