from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)
        
    def go_up(self):
        x_axis = self.xcor()
        y_axis = self.ycor()+20
        self.goto(x=x_axis,y=y_axis)
    def go_down(self):
        x_axis = self.xcor()
        y_axis = self.ycor()-20
        self.goto(x=x_axis,y=y_axis)
    