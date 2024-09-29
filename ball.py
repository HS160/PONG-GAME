from turtle import Turtle

class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        
        x_axis = self.xcor()+self.x_move
        Y_axis = self.ycor()+self.y_move
        self.goto(x_axis,Y_axis)
    
    def paddle_coll(self):
        self.x_move *= -1
        
    def bounce(self):
        self.y_move *= -1