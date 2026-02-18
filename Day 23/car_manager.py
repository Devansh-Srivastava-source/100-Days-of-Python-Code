from turtle import Turtle
import random 
COLORS = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'purple']
MOVE_DISTANCE = 5
class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.generate()

    def generate(self):
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
    
    def move(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    # def speed_up():
    #     MOVE_DISTANCE += 10
