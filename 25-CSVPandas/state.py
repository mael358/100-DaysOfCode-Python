from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 9, "normal")


class State(Turtle):

    def __init__(self, state_name, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write(state_name, align=ALIGNMENT, font=FONT)

