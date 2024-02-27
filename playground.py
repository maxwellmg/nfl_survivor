from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
 
'''
# Using current time
ini_time_for_now = datetime.now()
 
# printing initial_date
print ("initial_date", str(ini_time_for_now))
 
# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + \
                        timedelta(days = 730)
 
future_date_after_2days = ini_time_for_now + \
                         timedelta(days = 3)
print(future_date_after_2days)'''


'''year = 2000
week = 1
year_week_dict = {}

while count <= 2024:
    week = 1
    if week == 19:'''

year_week_list = []
#year_week_list.append(str(year) + "*" + str(week))
'''
for year in range(2021, 2024):
    for week in range(1, 19):
        if week == 0:
            pass
        else:
            year_week_list.append('"' + str(year) + "*" + str(week) + '", ')

with open("google_api_inputs.txt", "a") as f:
    for item in year_week_list:
        f.write(item)
f.close()'''

# Building perfect search
site = "site:espn.com" 
#allintitle:	Search for pages with multiple words in the title tag. 	allintitle:apple iphone

#before:	Search for results from before a particular date.	apple before:2007-06-29
#after:	Search for results from after a particular date.

# example #
example_search = "site:espn.com before:2018-11-14 after:2018-11-12 nfl week 11 power rankings"

#to_do_next 
#     find each week 1 sunday date for given year range
week_1_sundays = {2000: "09-03-2000", 2001: "09-09-2001", 2002: "09-05-2002", 2003: "09-04-2003", 2004: "09-09-2004", 2005: "09-08-2005", 2006: "09-07-2006", 2007: "09-06-2007", 2008: "09-04-2008", 2009: "09-10-2009", 2010: "09-09-2010", 2011: "09-11-2011", 2012: "09-09-2012", 2013: "09-08-2013", 2014: "09-07-2014", 2015: "09-13-2015", 2016: "09-11-2016", 2017: "09-10-2017", 2018: "09-09-2018", 2019: "09-08-2019", 2020: "09-13-2020", 2021: "09-12-2021", 2022: "09-11-2022", 2023: "09-10-2023"}



'''
custom_date = "09-03-2000"
date = datetime.strptime(custom_date, "%m-%d-%Y").date()
wednesday_after = date + \
                timedelta(days = 3)
print(wednesday_after)'''

#print(date)
#week_1s = []


# Good except prints doesnt output week 18 for years 2021-2023 and week 1 dates
all_weeks = []
'''
for week_1 in week_1_sundays.values():
    date = datetime.strptime(week_1, "%m-%d-%Y").date()
    post_draft = date - relativedelta(months=6)
    current_week = "week 1"
    all_weeks.append(current_week + "*" + str(post_draft) + "*" + str(date))
    for week in range(2, 18):
        if week == 2:
            date = datetime.strptime(week_1, "%m-%d-%Y").date()
            thursday_after = date + \
                        timedelta(days = 4)
            all_weeks.append("week 2" + "*" + str(date) + "*" + str(thursday_after))
        else:
            current_week = "week " + str(week)
            timedelta_multiplier = 7 * (week - 2)
            date = datetime.strptime(week_1, "%m-%d-%Y").date()
            current_date = date + \
                    timedelta(days = timedelta_multiplier)
            current_thursday = date + \
                    timedelta(days = 4 + timedelta_multiplier)
            all_weeks.append(current_week + "*" + str(current_date) + "*" + str(current_thursday))


#all_weeks_reversed = all_weeks.reverse()
print(list(reversed(all_weeks)))
'''
import json
#     create a time delta to span from sunday to thursday for each week in each season
#     append google_api_inputs list to contain "site"
'''
test_dict = {}
for i in range(1, 4):
    test_dict.update({str(i), str(i + 1)})
    print(test_dict)
print(test_dict)'''
'''test_dict = {}
list_a = ["A", "B", "C"]
#dict = {'key1': 'geeks', 'key2': 'for'}
for item in list_a:
    print("Current Dict is:" , test_dict)
    concat = item + "1"
    # adding key3
    test_dict.update({item: concat})
    print("Updated Dict is:", test_dict)
print(test_dict)

with open("power_rankings.json") as f:
    data = json.load(f)
    data.append(test_dict)
with open("power_rankings.json", "w") as f:
    json.dump(data, f)
f.close()'''
'''
def overwrite_save(variables, words_found, score, user_choice):
    with open("savefile.json") as f:
        data = json.load(f)
    new_save_dict = {'letters': variables, 'words_found': words_found, 'score': score, 'last updated': time.strftime("%m/%d/%Y %H:%M")}
    data.remove(user_choice)
    data.append(new_save_dict)
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    f.close()'''
'''
with open ("power_rankings.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    for item in data:

f.close()'''

sample_dict = {'nfl week 9 power rankings site:espn.com after:2021-10-31 before:2021-11-04 ': 'https://www.espn.com/nfl/story/_/page/NFLpowerranking1102/nfl-power-rankings-week-9-1-32-poll-plus-team-biggest-weakness-going-forward', 'nfl week 8 power rankings site:espn.com after:2021-10-24 before:2021-10-28 ': 'https://www.espn.com/nfl/story/_/page/NFLpowerranking1026/nfl-power-rankings-week-8-1-32-poll-plus-one-thing-got-wrong-every-team'}

# extracts relevant info from query to add to csv/json
for k, v in sample_dict.items():
    parsing = k.split(" ")
    week = " ".join(parsing[1:3])
    year = parsing[6].split(":")[1].split("-")[0]
    month = parsing[6].split(":")[1].split("-")[1]
    if month == "01":
        year = str(int(year) - 1)
    #print(year)
    #print(month)
    #print(week)