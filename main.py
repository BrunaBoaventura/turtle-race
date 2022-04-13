from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

y_relative = -75
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_relative)
    y_relative += 30
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True
else:
    print("Please choose an available color")

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning color is {winning_color}.")
            else:
                print(f"You lost. The winning color is {winning_color}.")

    rand_distance = randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()
