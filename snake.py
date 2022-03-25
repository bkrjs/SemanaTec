"""
Authors: Authors: Rebeca Rojas Pérez A01751192
         Juan Carlos Jiménez Tapia A01750115

Snake, classic arcade game.
"""

from random import randrange, choice, randint
from turtle import *
from xxlimited import foo

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Available colors for the snake and the food
colors = ["orange", "black", "pink", "green", "blue", "purple"]

# Pick a color for the food, delete it from the list to prevent choosing
# the same for the snake, and pink a color for the snake
foodColor = choice(colors)
colors.remove(foodColor)
snakeColor = choice(colors)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def moveFood():
    """"Move food randomly one step at a time."""
    global food
    if inside(food):
        #Where the food is moving
        aimFood =  vector(randint(-2, 2) * 10, randint(-2, 2) * 10)
        food.move(aimFood)
    else: 
        food = vector(0, 0)

    ontimer(moveFood, 1000)


def move():
    """Move snake forward one segment at a time."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-1, 2) * 10
        food.y = randrange(-1, 2) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
