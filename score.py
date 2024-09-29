from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(position)
        self.score_update()
        
    def score_update(self):
        self.clear()
        self.write(f"{self.score}",align="center",font=('Arial',24,'normal'))
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()