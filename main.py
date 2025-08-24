# with open("weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)

import csv

with open("weather_data.csv") as file:
    contents = csv.reader(file)
    for row in contents:
        print(row)