# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# REEBORG HURDLE 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# REEBORG HURDLE 2 CHALLENGE USING WHILE LOOPS


def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# FIRST ATTEMPT    
number_of_hurdles = 6
while number_of_hurdles > 0:
    if at_goal() != True:
        jump_hurdle()
        number_of_hurdles -= 1
    else:
        number_of_hurdles = 0
        print("Reeborg made it to the goal!")

# SECOND ATTEMPT, CLEANER WAY TO CODE THIS
while not at_goal():
    jump_hurdle()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# REEBORG HURDLE 3 CHALLENGE USING WHILE LOOPS + IF STATEMENTS

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()


# REEBORG HURDLE 4 CHALLENGE

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_right():
    turn_right()
    move()
    turn_right()
while not at_goal():
    if front_is_clear() and is_facing_north() and wall_on_right():
        move()
    elif front_is_clear and is_facing_north() and not wall_on_right():
        move_right()
    elif wall_in_front():
        turn_left()
    else:
        move()