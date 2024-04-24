import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turned off tracer, instead the screen is updated every 0.1 sec in the while loop
screen.title("Turtle Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for player control
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
cars_moving = True
cycle_counter = 1
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    # spawning a new car every 6th cycle and if cars should be moving
    if ((cycle_counter % 6) == 0) & cars_moving:
        car_manager.new_car()

    if cars_moving:
        car_manager.move_all_cars()

    for car in car_manager.cars:
        # Detect collision with car
        if player.distance(car) < 25:
            cars_moving = False
            scoreboard.display_game_over()
            break

        # Detect reaching the finish line
        if player.crossed_finish_line():
            scoreboard.increase_level()
            player.return_to_start()
            car_manager.car_speed *= 0.9  # increasing car speed by 10%

    cycle_counter += 1
