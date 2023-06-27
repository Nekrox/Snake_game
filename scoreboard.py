from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALGNM = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.current_score = -1

        with open("data.txt", mode="r") as file:
            self.highest_score = int(file.read())

        self.write_score()

    def write_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score} High score: {self.highest_score}", move=False, align=ALGNM, font=FONT)

    def reset(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.current_score = -1
        self.write_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", move=False, align=ALGNM, font=FONT)
