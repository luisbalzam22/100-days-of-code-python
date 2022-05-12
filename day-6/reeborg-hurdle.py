def turn_right():
    turn_left()
    turn_left()
    turn_left()

def skip_fence():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
   
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        skip_fence()