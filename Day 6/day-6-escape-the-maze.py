# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


# REEBORG MAZE MAP SOLUTION

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_right():
    turn_right()
    move()
    turn_right()
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif front_is_clear and not wall_on_right():
        turn_right()
        move()
    else:
        move()


# REEBORG MAZE MAP REFACTORED, BUT CAN CAUSE INFINITE LOOP IN SOME CASES

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_right():
    turn_right()
    move()
    turn_right()
while not at goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# REEBORG MAZE MAP REFACTORED TO CAUSE ZERO INFINITE LOOPS, TESTED OUT WITH PROBLEM WORLD JSON FILES!! YAY!

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_right():
    turn_right()
    move()
    turn_right()
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif front_is_clear and not wall_on_right and is_facing_north():
        turn_right()
        move()
    elif front_is_clear and right_is_clear():
        move()
    else:
        move()

# INSTRUCTOR SOLUTION THAT TESTS OUT WITH PROBLEM WORLD JSON FILES

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_right():
    turn_right()
    move()
    turn_right()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
