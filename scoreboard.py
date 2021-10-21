from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")
FONT1 = ("Courier", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 220)
        self.write(arg=f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(arg=f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def add_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def add_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_left(self):
        self.goto(0, 0)
        self.write(arg="Game Over.\nPLAYER 1 WINS!", align=ALIGNMENT, font=FONT1)

    def game_over_right(self):
        self.goto(0, 0)
        self.write(arg="Game Over.\nPLAYER 2 WINS!", align=ALIGNMENT, font=FONT1)
