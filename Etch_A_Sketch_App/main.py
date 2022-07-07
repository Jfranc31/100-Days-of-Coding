from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(1000, 700)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    # or tim.setpos(0, 0) tim.setheading(0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
