from turtle import Turtle
import random

# You can change the Food's Color and Shape here:
FOOD_SHAPE = "circle"
FOOD_COLOR = "blue"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 250)
        self.goto(rand_x, rand_y)
