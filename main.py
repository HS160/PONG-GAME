from turtle import Turtle, Screen, textinput
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time

def clear_and_replay():
    global screen
    screen.clear()
    screen.bgcolor('black')
    replay = textinput("Replay", "Do you want to play again? (yes/no)").lower()
    if replay == 'yes':
        return True
    return False

def setup_game():
    global screen, scoreboard_l, scoreboard_r, r_paddle, l_paddle, ball, time_interval
    
    screen.setup(width=800, height=600)
    screen.title("PONG GAME")
    screen.tracer(0)
    screen.listen()

    scoreboard_l = Scoreboard((-100, 250))
    scoreboard_r = Scoreboard((100, 250))
    r_paddle = Paddle((370, 0))
    l_paddle = Paddle((-370, 0))
    ball = Ball((0, 0))

    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    time_interval = 0.1

def game_loop():
    global time_interval
    while True:
        time.sleep(time_interval)
        screen.update()
        ball.move()
        
        if ball.ycor() > 290 or ball.ycor() < -280:
            ball.bounce()
            
        if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
            ball.paddle_coll()
            scoreboard_l.score_update()
            if time_interval > 0.01:
                time_interval -= 0.01
            
        if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
            ball.paddle_coll()
            scoreboard_r.score_update()
            if time_interval > 0.01:
                time_interval -= 0.01
            
        if ball.xcor() > 370:
            scoreboard_l.increase_score()
            time_interval = 0.1
            ball.goto(0, 0)
        if ball.xcor() < -370:
            scoreboard_r.increase_score()
            time_interval = 0.1
            ball.goto(0, 0)

        if not screen.getcanvas().winfo_exists():
            return False

        yield

# Initialize the screen
screen = Screen()
screen.bgcolor('black')

# Main game loop
while True:
    setup_game()
    game = game_loop()
    
    def check_replay():
        if clear_and_replay():
            screen.clear()
            screen.bgcolor('black')
        else:
            screen.bye()
            return
        
        for _ in game:
            if not screen.getcanvas().winfo_exists():
                return
        check_replay()

    screen.onkey(check_replay, 'c')
    
    for _ in game:
        if not screen.getcanvas().winfo_exists():
            break

    if not screen.getcanvas().winfo_exists():
        break

print("Game Over")