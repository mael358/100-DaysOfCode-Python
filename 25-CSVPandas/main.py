import pandas, statistics, turtle
from state import State

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index != 0:
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# # data_dict = data.to_json()
# # print(data_dict)
# #
# # print(data["temp"].mean())
# #
# # print(data["temp"].max())
# #
# # # Get data in columns
# # # print(data["condition"])
# # print(data.condition)
#
# # print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# 1. Read the CSV data
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# # 2. Get the Gray, Red and Black numbers
# gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
# gray_squirrel_list = gray_squirrel["Primary Fur Color"].to_list()
# print(len(gray_squirrel_list))
#
# red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
# red_squirrel_list = red_squirrel["Primary Fur Color"].to_list()
# print(len(red_squirrel_list))
#
# black_squirrel = data[data["Primary Fur Color"] == "Black"]
# black_squirrel_list = black_squirrel["Primary Fur Color"].to_list()
# print(len(black_squirrel_list))
#
# # 3. Create a list of the 3 counts
# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [len(gray_squirrel_list), len(red_squirrel_list), len(black_squirrel_list)]
# }
#
# # 4. Convert list to a csv file
# pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_states = 0
correct_guesses = []

# 1. Read the CSV data
data = pandas.read_csv("50_states.csv")

# 2. Create the loop of the prompt
while True:
    if correct_states == 50:
        break
    answer_state = screen.textinput(title=f"{correct_states}/50 States correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break

    state_data = data[data["state"].str.lower() == answer_state.lower()]
    state_name = state_data.iloc[0]['state']
    if not state_data.empty and state_name not in correct_guesses:
        state = State(state_name, int(state_data['x']), int(state_data['y']))
        correct_states += 1
        correct_guesses.append(state_name)


# Save the missing states
if correct_guesses != 50:
    df = data[~data['state'].isin(correct_guesses)]

    df.to_csv('data_to_learn.csv', index=False)