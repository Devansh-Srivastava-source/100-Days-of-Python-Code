## Day 6 - Functions and Karel

## Project
- Escaping the maze
- All the coding part of this project is on the website of Reeborg's world.

## What I learnt
- Defining and calling functions
- indentation importance in python
- more about while loops
- running various commands on Reeborg's World website
- This is the code which solves all 4 levels of Hurdles as well as the maze problem.
But one position of bot which is (x,y) = (4,4), this code fails and creates an infinite loop.
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
        
    while not at_goal():
        if right_is_clear():
            turn_right()
        if wall_in_front():
            turn_left()
        if front_is_clear():
            move()