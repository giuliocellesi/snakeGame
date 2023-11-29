from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(0, 268)
        self.write(f"Score: {self.score}. High score: {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def increseScore(self):
        self.score += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.write(f"Game over.", align="center", font=("Courier", 20, "normal"))
        self.goto(0, -30)
        self.write(f"Press a key to start again..", align="center", font=("Courier", 12, "normal"))
        self.score = 0


