import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        # Makes a csv with the states that were missed.
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        
    if answer_state in all_states:
        guessed_states.append(answer_state)
        State = data[data.state == answer_state]
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.setposition(int(State.x), int(State.y))
        state_name.write(answer_state)

if len(guessed_states) == 50:
    finished = turtle.Turtle()
    finished.penup()
    finished.hideturtle()
    finished.setposition(x=-430, y=-300)
    finished.write(arg="You've guessed all the States correctly!", font=("Courier", 35, "bold"))

screen.exitonclick()
