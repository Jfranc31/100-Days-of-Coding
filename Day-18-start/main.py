from turtle import Turtle, Screen
import random
import time

# can give alias to module, like, import turtle as t
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# arrow = Turtle()
# arrow.shape("arrow")
# arrow.color("black")
# for _ in range(15):
#     arrow.forward(10)
#     arrow.penup()
#     arrow.forward(10)
#     arrow.pendown()




start = time.time()
colors = ["dark slate blue", "slate blue", "indigo", "orchid", "magenta", "dark magenta",
          "deep pink", "pink", "salmon", "crimson", "orange red", "red", "yellow", "lime", "green", "cyan",
          "blue", "gray"]
arrow = Turtle()
arrow.shape("arrow")
arrow.speed(10)
for number_of_sides in range(3, 40):
    angle = 360 / number_of_sides
    arrow.color(random.choice(colors))
    for y in range(number_of_sides):
        arrow.forward(100)
        arrow.right(angle)

end = time.time()
print(end-start)
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
