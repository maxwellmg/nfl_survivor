'''year = 2000
week = 1
year_week_dict = {}

while count <= 2024:
    week = 1
    if week == 19:'''

year_week_list = []
#year_week_list.append(str(year) + "*" + str(week))

for year in range(2021, 2024):
    for week in range(1, 19):
        if week == 0:
            pass
        else:
            year_week_list.append('"' + str(year) + "*" + str(week) + '", ')

with open("google_api_inputs.txt", "a") as f:
    for item in year_week_list:
        f.write(item)
f.close()