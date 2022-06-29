# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data_one = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print(data_list)
# print(data["temp"].mean())
# print(data["temp"].sum())
# print(data["temp"].max())
# total_temp = 0
#
# for temps in data_list:
#     total_temp = total_temp + temps
#
# print(total_temp)
# avg = total_temp / len(data_list)
# print(avg)

# print(data_one[data_one.temp == data_one.temp.max()])
# sunday = (data[data.day == "Sunday"])
# print(sunday.temp)

# data_dict = {'Name': ['Karan', 'Rohit', 'Sahil', 'Aryan'],
#              'Age': [23, 22, 21, 24]
#              }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")


# data_dict = data.to_dict()
# color = data_dict["Primary Fur Color"]
# gray_count = 0
# black_count = 0
# cinnamon_count = 0
# for keys in color:
#     if color[keys] == "Gray":
#         gray_count += 1
#     elif color[keys] == "Black":
#         black_count += 1
#     elif color[keys] == "Cinnamon":
#         cinnamon_count += 1
#
# print(gray_count)
# print(black_count)
# print(cinnamon_count)
# print(data[data["Primary Fur Color"] == "White"])
# print(data[data.temp == data.temp.max()])
# sunday = (data[data.day == "Sunday"])
# print(sunday.temp)
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_color = (data[data["Primary Fur Color"] == "Gray"])
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours_data = data["Primary Fur Color"].value_counts()
colours_data.to_csv("Squirrel_colour_data.csv")
