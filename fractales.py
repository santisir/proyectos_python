from math import ceil
from operator import le
from turtle import *
import random as rd

speed(-3)

def tree(size, levels, angle):
    if levels==0:
        colors = ['red', 'blue', 'yellow', 'green', 'pink', 'brown', 'orange', 'grey', 'purple'] 
        color(rd.choice(colors))
        dot(size)
        color('black')

        return
    
    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

# left(90)
# backward(200)
# tree(100, 6, 30)

def snowflake_side(lenght, levels):
    if levels == 0:
        forward(lenght)
        return
    lenght /= 3.0
    snowflake_side(lenght, levels - 1)
    left(60)
    snowflake_side(lenght, levels - 1)
    right(120)
    snowflake_side(lenght, levels - 1)
    left(60)
    snowflake_side(lenght, levels - 1)

def create_snowflake(lenght, sides):
    colors = ['red', 'blue', 'yellow', 'green', 'pink', 'brown', 'orange', 'grey', 'purple']
    for i in range(sides):
        color(rd.choice(colors))
        snowflake_side(lenght, 4)
        right(360/sides)

# create_snowflake(150, 5)
tree(100,7,70)
left(180)
tree(100,7,70)
mainloop()