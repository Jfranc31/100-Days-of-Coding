# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["day"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()

# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
# avg_temp = total_temp / len(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)

# avg_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# print(max_temp)
# print(temp_list)

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Creat a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]
squirrels_count = fur_data.value_counts()
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrels_count[0], squirrels_count[1], squirrels_count[2]]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
