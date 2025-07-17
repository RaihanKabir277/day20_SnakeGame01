
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = self.file_read()
        # ------another way to do this -------
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        
    # def file_read(self):
    #     with open("data.txt", "r") as file:
    #         return file.read()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

# now we update the game and do not game over this ...
    # def game_over(self):
    #     self.goto(0,0)  #center of the screen
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)  

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
