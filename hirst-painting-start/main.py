# ##This code will not work in repl.it as there is no access to the color gram package here.###
# #We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# TODO - 10 by 10 dots
# TODO -  Dot size is 20 and spaced by 50

import turtle as t
import random

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

arrow = t.Turtle()
screen = t.Screen()
arrow.shape("arrow")
t.colormode(255)
arrow.penup()
arrow.hideturtle()
arrow.speed("fastest")
pos = -150

for column in range(10):
    arrow.setpos(-200, pos)
    pos += 50
    for row in range(10):
        arrow.dot(20, random.choice(color_list))
        arrow.forward(50)

screen.exitonclick()
