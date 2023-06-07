import random
import turtle
import time

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.penup()
turtle_instance.speed(0)


score_write = turtle.Turtle()
score_write.penup()
score_write.speed(0)
score_write.sety(250)

score_count = 0

score_write.write("Score: {} ".format(score_count),align="center",font=("Arial",24,"bold"))
def counter2(count):
    count_write = turtle.Turtle()
    count_write.penup()
    count_write.speed(0)
    count_write.sety(200)


    while count>=0:

        spawn_turtle()
        count_write.clear()
        count_write.write("Kalan sure: {} saniye".format(count),align="center", font=("Arial", 24,"bold"))
        count -=1
        time.sleep(1)
    count_write.clear()
    count_write.write("Game Over!".format(count),align="center", font=("Arial",24,"bold"))
    turtle.done()

def spawn_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle_instance.goto(x, y)

def score(x,y):
    global score_count
    score_count+=1
    score_write.clear()
    score_write.write("Score: {} ".format(score_count),align="center",font=("Arial",24,"bold"))

turtle.onscreenclick(score)
counter2(10)
turtle_instance.onclick(score)
