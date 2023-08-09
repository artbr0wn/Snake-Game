from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
           self.high_score = int(data.read())
        # scoreboard = print(f"Your score: {score}")
        self.ht()
        self.goto(x=0, y=280)
        self.color('white')
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()
