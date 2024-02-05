#bet, bet , bet
#pathing
import turtle
import time

WIDTH, HEIGHT = 500, 500



def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter the number of racing turtles (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is invalid. Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not valid! Not in range 2-10. ")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("turtle_racing")

racers = get_number_of_turtles()
init_turtle()

racer = turtle.Turtle()
racer.speed(1)
racer.forward(100)
racer.left(90)
racer.backward(80)
racer.left(90)
racer.forward(120)
racer.forward(100)
racer.left(90)
racer.backward(80)
racer.left(90)
racer.forward(120)
racer.forward(100)
racer.left(90)
racer.backward(80)
racer.left(90)
racer.forward(120)


time.sleep(50)