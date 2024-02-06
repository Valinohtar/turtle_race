
#pathing
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'black', 'pink', 'cyan', 'grey']


def race(colors):
    turtles = create_turtles(colors)
    
    direction_list = ['far_right', 'right', 'left', 'far_left']
    while True:
        for racer in turtles:
            racer.forward(random.randint(5, 15))


            direction = random.choice(direction_list)
            if direction == direction_list[0]:
                racer.right(random.randint(10, 14))
            elif direction == direction_list[1]:
                racer.right(random.randint(1, 10))
            elif direction == direction_list[2]:
                racer.left(random.randint(1, 10))
            elif direction == direction_list[3]:
                racer.left(random.randint(10, 14))


            x, y = racer.pos()
            if x <= -(WIDTH//2)+10:
                racer.right(random.randint(20, 30))
            if x >= WIDTH//2-10:
                racer.left(random.randint(20,30))

            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
                

def get_bet(colors):
    bet = input(f"Please choose which turtle wins the race! Turtles: {colors}" )
    while bet not in colors:
        bet = input(f"Wrong colour, please give the one mentioned in the list: {colors} ")
    bet = str(bet)
    return bet


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

def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos((500/(len(colors)+1))*(i+1)-250, -225)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("turtle_racing")

racers = get_number_of_turtles()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
bet = get_bet(colors)

winner = race(colors)
print(f'Winner is: {winner}')
if bet == winner:
    print("Your bet was right! A certificate will be printed out!")
    with open("Certificate.txt", "w") as f:
        f.write("Congratulations!\n")
        f.write(f"Your bet that {winner} wins was correct.")



time.sleep(5)