from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 260)
        self.level = 0
        self.next_level()
    
    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align = "center", font = FONT)

    # def game_over(self):
    #     self.write("GAME OVER", align= "center", font= FONT)


    # def next_level(self):


    
        