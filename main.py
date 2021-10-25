from turtle import *
from states import all_states
import pandas

#Declaring constants
ALIGN = "center"
FONT = ("Arial", 10, "normal")

#Create Screen object
screen = Screen()

#set background image and title
MAP = 'india_map.gif'
screen.bgpic(MAP)
screen.title("Indian State Game")

#Create Turtle object
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed(10)


state_index = 0
inputs = []
missing_data = []
"""
we can create state_data.csv by getting x and y coordinates on click
and save it to state_date.csv.
As I have create it so I comment it. 

def get_mouse_click_pos(x, y):
    global state_index
    if state_index < len(all_states):
        with open("state_data.csv", "a") as file:
            file.write(f"{all_states[state_index]},{x},{y}")

        state_index = state_index + 1


screen.onscreenclick(get_mouse_click_pos())
"""

state_index = 1

#Read positions of state from state_data.csv
data = pandas.read_csv("state_data.csv")

#Function which write state name on state position
def write(input):
    row = data[data.State == input]
    xcor = int(row.XCOR)
    ycor = int(row.YCOR)
    turtle.goto(xcor, ycor)
    turtle.write(input, align=ALIGN, font=FONT)
    inputs.append(input)

#Loop till all the states are guessed
while len(inputs) < 31:

    #Taking user input
    user_input = screen.textinput(f"{len(inputs)}/{len(all_states)}", "Enter State name. Enter 'exit' to quit").title().strip()

    #Exception case for Jammu and kashmir
    if user_input.lower() == "jammu and kashmir":
        user_input = 'Jammu and Kashmir'

    #If user_input is correct and not given prior
    if user_input in all_states and user_input not in inputs:
        write(user_input)

    #If user type exit, write all remaining states
    if user_input.lower() == "exit":
        for state in all_states:
            if state not in inputs:
                write(state)
                missing_data.append(state)
        new_data = pandas.DataFrame(missing_data)

        #print unguessed state to console
        print(new_data)

        done()

done()
