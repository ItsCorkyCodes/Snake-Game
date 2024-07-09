from turtle import Turtle

FONT = ("Futura", 17, "normal")
POSITION = (0, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        # Read from data.txt and make high_score
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())

        self.score = 0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(POSITION)
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", True, "center", FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as data_file:
            data_file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def give_point(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", True, "center", ("Futura", 20, "bold"))
    #     self.goto(0, -40)
    #     self.write("Click Screen and Run Again to Retry", True, "center", ("Futura", 16, "normal"))
