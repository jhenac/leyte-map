import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 650)
screen.title("Leyte Province")
image = "leyte_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("towns_and_cities.csv")

all_towns = data.towns.to_list()
correct_answers = []

while len(correct_answers) < len(all_towns):
    answer_town = screen.textinput(f"{len(correct_answers)}/{len(all_towns)} Towns Correct",
                                    "What's another town name?").title()
    if answer_town.lower() == "exit":
        missing_towns = []
        for town in all_towns:
            if town not in correct_answers:
                missing_towns.append(town)
        df = pandas.DataFrame(missing_towns, columns=["towns"])
        df.to_csv("towns_to_learn.csv", index=False)
        break
    if answer_town in all_towns and answer_town not in correct_answers:
        correct_answers.append(answer_town)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        town_data = data[data.towns == answer_town]
        town_x = int(town_data.x)
        town_y = int(town_data.y)
        t.goto(town_x, town_y)
        t.write(answer_town)

screen.exitonclick()

