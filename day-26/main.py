numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [number**2 for number in numbers]

# Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)

with open("file1.txt") as file1:
    numbers_1 = file1.readlines()
with open("file2.txt") as file2:
    numbers_2 = file2.readlines()
results = [int(num) for num in numbers_1 if num in numbers_2]

# Write your code above 👆

print(results)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

sentence_dict = {word: len(word) for word in sentence.split()}

print(sentence_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items()}

print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
