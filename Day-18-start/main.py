import turtle
# from turtle import Turtle, Screen
import random
import turtle as t
import time

# can give alias to module, like, import turtle as t
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# ## Make a straight dotted line
# arrow = Turtle()
# arrow.shape("arrow")
# arrow.color("black")
# for _ in range(15):
#     arrow.forward(10)
#     arrow.penup()
#     arrow.forward(10)
#     arrow.pendown()

# ## Make shapes with different color increasing from 3 sides and up
# start = time.time()
# colors = ["dark slate blue", "slate blue", "indigo", "orchid", "magenta", "dark magenta",
#           "deep pink", "pink", "salmon", "crimson", "orange red", "red", "yellow", "lime", "green", "cyan",
#           "blue", "gray"]
# arrow = Turtle()
# arrow.shape("arrow")
# arrow.speed(10)
# for number_of_sides in range(3, 40):
#     angle = 360 / number_of_sides
#     arrow.color(random.choice(colors))
#     for y in range(number_of_sides):
#         arrow.forward(100)
#         arrow.right(angle)
#
# end = time.time()
# print(end-start)
# arrow = Turtle()
# colors = ["dark slate blue", "slate blue", "indigo", "orchid", "magenta", "dark magenta",
#           "deep pink", "pink", "salmon", "crimson", "orange red", "red", "yellow", "lime", "green", "cyan",
#           "blue", "gray"]
# directions = [0, 90, 180, 270]
# arrow.shape("arrow")
# arrow.pensize(20)
# arrow.speed(10)
# for number_of_steps in range(100):
#     arrow.color(random.choice(colors))
#     arrow.forward(50)
#     arrow.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

# tim = Turtle()
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# ########### Challenge 5 - Spirograph ########
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = t.Screen()

angle = 0
tim.speed("fastest")
for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    angle += 5
    tim.setheading(angle)
screen.exitonclick()

# or

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)
# screen.exitonclick()
