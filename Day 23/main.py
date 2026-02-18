from turtle import Screen
from player import Player
import car_manager
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The crossroad game")
screen.tracer(0)

player = Player()
Cars = [] # List where all car objects will be stored
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
# def quitting():
#     game_is_on = False
# screen.onkey(quitting,"q")
i=0
while game_is_on:
    # Generation of new cars and storing in a list
    if(i%6 == 0):
        car = car_manager.Car()
        Cars.append(car)

    # Condition of next level
    if player.ycor() > 280:
        scoreboard.next_level()
        player.reset_position()
        car_manager.MOVE_DISTANCE += 3

    # Time delay to make animaitons smoother
    time.sleep(0.1)
    screen.update()

    # Moving the cars and removing from list if they have crossed the screen.
    for car in Cars:
        car.move()
        if car.xcor() < -320:
            Cars.remove(car)
            
    # This variable is contributing in car generation, every sixth loop generates a car.
    i += 1

    #Detection of collision with a car
    for car in Cars:
        if player.distance(car) < 25:
            game_is_on = False
            player.write("GAME OVER", align= "center", font= ("Courier", 30, "normal"))



screen.exitonclick()