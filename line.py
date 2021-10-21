from turtle import Turtle


class Line:
    def __init__(self):
        self.line = Turtle()
        self.draw_line()

    def draw_line(self):
        self.line.hideturtle()
        self.line.goto(0, -300)
        self.line.setheading(90)
        while self.line.ycor() < 300:
            self.line.color("white")
            self.line.penup()
            self.line.forward(20)
            self.line.pendown()
            self.line.forward(20)
