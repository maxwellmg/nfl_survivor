from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
#from function_library import week1s_to_all_search_inputs
 
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

sample_dict = {'nfl week 10 power rankings site:espn.com after:2021-10-31 before:2021-11-04 ': 'https://www.espn.com/nfl/story/_/page/NFLpowerranking1102/nfl-power-rankings-week-9-1-32-poll-plus-team-biggest-weakness-going-forward', 'nfl week 8 power rankings site:espn.com after:2021-10-24 before:2021-10-28 ': 'https://www.espn.com/nfl/story/_/page/NFLpowerranking1026/nfl-power-rankings-week-8-1-32-poll-plus-one-thing-got-wrong-every-team'}
'''
# extracts relevant info from query to add to csv/json
for k, v in sample_dict.items():
    parsing = k.split(" ")
    print(parsing)
    week = parsing[2]
    year = parsing[6].split(":")[1].split("-")[0]
    month = parsing[6].split(":")[1].split("-")[1]
    if month == "01":
        year = str(int(year) - 1)
    #print(year)
    #print(month)
    print(week)'''



'''
def week1s_to_all_search_inputs(week_1_date_dict):
    week_1_sundays = week_1_date_dict
    all_weeks = []
    for week_1 in week_1_sundays.values():
        date = datetime.strptime(week_1, "%m-%d-%Y").date()
        current_week = "week 1"
        wednesday_after = date + \
                            timedelta(days = 6)
        all_weeks.append(current_week + "*" + str(date) + "*" + wednesday_after)
        for week in range(2, 18):
            if week == 2:
                date = datetime.strptime(week_1, "%m-%d-%Y").date() + \
                            timedelta(days = 7)
                wednesday_after = date + \
                            timedelta(days = 13)
                all_weeks.append("week 2" + "*" + str(date) + "*" + str(wednesday_after))
            else:
                current_week = "week " + str(week)
                timedelta_multiplier = 7 * (week - 2)
                date = datetime.strptime(week_1, "%m-%d-%Y").date() + \
                        timedelta(days = 5)
                current_date = date + \
                        timedelta(days = 5+ timedelta_multiplier)
                current_thursday = date + \
                        timedelta(days = 11 + timedelta_multiplier)
                all_weeks.append(current_week + "*" + str(current_date) + "*" + str(current_thursday))
    #special_list = list(reversed(all_weeks))
    print(all_weeks)
    #print(special_list)'''
'''with open("THUR_2_MON_dates.txt", "a") as f:
    for line in all_weeks:
        f.write(line)
        f.write(", ")
f.close()'''


    #week1s_to_all_search_inputs(week_1_sundays)

'''
from datetime import datetime, timedelta

nfl_week_list = []

dates_dict = {
    2000: "09-03-2000", 2001: "09-09-2001", 2002: "09-05-2002", 2003: "09-04-2003", 2004: "09-09-2004", 2005: "09-08-2005", 2006: "09-07-2006", 2007: "09-06-2007", 2008: "09-04-2008", 2009: "09-10-2009", 2010: "09-09-2010", 2011: "09-11-2011", 2012: "09-09-2012", 2013: "09-08-2013", 2014: "09-07-2014", 2015: "09-13-2015", 2016: "09-11-2016", 2017: "09-10-2017", 2018: "09-09-2018", 2019: "09-08-2019", 2020: "09-13-2020", 2021: "09-12-2021", 2022: "09-11-2022", 2023: "09-10-2023"
}

for year, start_date_str in dates_dict.items():
    start_date = datetime.strptime(start_date_str, "%m-%d-%Y")

    for i in range(17):
        end_date = start_date + timedelta(days=6)
        nfl_week_list.append('"' + f"week_{i + 1}*{start_date.strftime('%m-%d-%Y')}*{end_date.strftime('%m-%d-%Y')}" + '", ')
        start_date = end_date + timedelta(days=1)
    #print()

with open("nfl_thursday_to_wednesday.txt", "a") as f:
    for line in nfl_week_list:
        f.write(line)
f.close()

'''

import csv
from datetime import datetime

# Define your list of date ranges with labels in the format 'week*mm-dd-yyyy*mm-dd-yyyy'
date_ranges_str = [
    "week_1*09-03-2000*09-09-2000", "week_2*09-10-2000*09-16-2000", "week_3*09-17-2000*09-23-2000", "week_4*09-24-2000*09-30-2000", "week_5*10-01-2000*10-07-2000", "week_6*10-08-2000*10-14-2000", "week_7*10-15-2000*10-21-2000", "week_8*10-22-2000*10-28-2000", "week_9*10-29-2000*11-04-2000", "week_10*11-05-2000*11-11-2000", "week_11*11-12-2000*11-18-2000", "week_12*11-19-2000*11-25-2000", "week_13*11-26-2000*12-02-2000", "week_14*12-03-2000*12-09-2000", "week_15*12-10-2000*12-16-2000", "week_16*12-17-2000*12-23-2000", "week_17*12-24-2000*12-30-2000", "week_1*09-09-2001*09-15-2001", "week_2*09-16-2001*09-22-2001", "week_3*09-23-2001*09-29-2001", "week_4*09-30-2001*10-06-2001", "week_5*10-07-2001*10-13-2001", "week_6*10-14-2001*10-20-2001", "week_7*10-21-2001*10-27-2001", "week_8*10-28-2001*11-03-2001", "week_9*11-04-2001*11-10-2001", "week_10*11-11-2001*11-17-2001", "week_11*11-18-2001*11-24-2001", "week_12*11-25-2001*12-01-2001", "week_13*12-02-2001*12-08-2001", "week_14*12-09-2001*12-15-2001", "week_15*12-16-2001*12-22-2001", "week_16*12-23-2001*12-29-2001", "week_17*12-30-2001*01-05-2002", "week_1*09-05-2002*09-11-2002", "week_2*09-12-2002*09-18-2002", "week_3*09-19-2002*09-25-2002", "week_4*09-26-2002*10-02-2002", "week_5*10-03-2002*10-09-2002", "week_6*10-10-2002*10-16-2002", "week_7*10-17-2002*10-23-2002", "week_8*10-24-2002*10-30-2002", "week_9*10-31-2002*11-06-2002", "week_10*11-07-2002*11-13-2002", "week_11*11-14-2002*11-20-2002", "week_12*11-21-2002*11-27-2002", "week_13*11-28-2002*12-04-2002", "week_14*12-05-2002*12-11-2002", "week_15*12-12-2002*12-18-2002", "week_16*12-19-2002*12-25-2002", "week_17*12-26-2002*01-01-2003", "week_1*09-04-2003*09-10-2003", "week_2*09-11-2003*09-17-2003", "week_3*09-18-2003*09-24-2003", "week_4*09-25-2003*10-01-2003", "week_5*10-02-2003*10-08-2003", "week_6*10-09-2003*10-15-2003", "week_7*10-16-2003*10-22-2003", "week_8*10-23-2003*10-29-2003", "week_9*10-30-2003*11-05-2003", "week_10*11-06-2003*11-12-2003", "week_11*11-13-2003*11-19-2003", "week_12*11-20-2003*11-26-2003", "week_13*11-27-2003*12-03-2003", "week_14*12-04-2003*12-10-2003", "week_15*12-11-2003*12-17-2003", "week_16*12-18-2003*12-24-2003", "week_17*12-25-2003*12-31-2003", "week_1*09-09-2004*09-15-2004", "week_2*09-16-2004*09-22-2004", "week_3*09-23-2004*09-29-2004", "week_4*09-30-2004*10-06-2004", "week_5*10-07-2004*10-13-2004", "week_6*10-14-2004*10-20-2004", "week_7*10-21-2004*10-27-2004", "week_8*10-28-2004*11-03-2004", "week_9*11-04-2004*11-10-2004", "week_10*11-11-2004*11-17-2004", "week_11*11-18-2004*11-24-2004", "week_12*11-25-2004*12-01-2004", "week_13*12-02-2004*12-08-2004", "week_14*12-09-2004*12-15-2004", "week_15*12-16-2004*12-22-2004", "week_16*12-23-2004*12-29-2004", "week_17*12-30-2004*01-05-2005", "week_1*09-08-2005*09-14-2005", "week_2*09-15-2005*09-21-2005", "week_3*09-22-2005*09-28-2005", "week_4*09-29-2005*10-05-2005", "week_5*10-06-2005*10-12-2005", "week_6*10-13-2005*10-19-2005", "week_7*10-20-2005*10-26-2005", "week_8*10-27-2005*11-02-2005", "week_9*11-03-2005*11-09-2005", "week_10*11-10-2005*11-16-2005", "week_11*11-17-2005*11-23-2005", "week_12*11-24-2005*11-30-2005", "week_13*12-01-2005*12-07-2005", "week_14*12-08-2005*12-14-2005", "week_15*12-15-2005*12-21-2005", "week_16*12-22-2005*12-28-2005", "week_17*12-29-2005*01-04-2006", "week_1*09-07-2006*09-13-2006", "week_2*09-14-2006*09-20-2006", "week_3*09-21-2006*09-27-2006", "week_4*09-28-2006*10-04-2006", "week_5*10-05-2006*10-11-2006", "week_6*10-12-2006*10-18-2006", "week_7*10-19-2006*10-25-2006", "week_8*10-26-2006*11-01-2006", "week_9*11-02-2006*11-08-2006", "week_10*11-09-2006*11-15-2006", "week_11*11-16-2006*11-22-2006", "week_12*11-23-2006*11-29-2006", "week_13*11-30-2006*12-06-2006", "week_14*12-07-2006*12-13-2006", "week_15*12-14-2006*12-20-2006", "week_16*12-21-2006*12-27-2006", "week_17*12-28-2006*01-03-2007", "week_1*09-06-2007*09-12-2007", "week_2*09-13-2007*09-19-2007", "week_3*09-20-2007*09-26-2007", "week_4*09-27-2007*10-03-2007", "week_5*10-04-2007*10-10-2007", "week_6*10-11-2007*10-17-2007", "week_7*10-18-2007*10-24-2007", "week_8*10-25-2007*10-31-2007", "week_9*11-01-2007*11-07-2007", "week_10*11-08-2007*11-14-2007", "week_11*11-15-2007*11-21-2007", "week_12*11-22-2007*11-28-2007", "week_13*11-29-2007*12-05-2007", "week_14*12-06-2007*12-12-2007", "week_15*12-13-2007*12-19-2007", "week_16*12-20-2007*12-26-2007", "week_17*12-27-2007*01-02-2008", "week_1*09-04-2008*09-10-2008", "week_2*09-11-2008*09-17-2008", "week_3*09-18-2008*09-24-2008", "week_4*09-25-2008*10-01-2008", "week_5*10-02-2008*10-08-2008", "week_6*10-09-2008*10-15-2008", "week_7*10-16-2008*10-22-2008", "week_8*10-23-2008*10-29-2008", "week_9*10-30-2008*11-05-2008", "week_10*11-06-2008*11-12-2008", "week_11*11-13-2008*11-19-2008", "week_12*11-20-2008*11-26-2008", "week_13*11-27-2008*12-03-2008", "week_14*12-04-2008*12-10-2008", "week_15*12-11-2008*12-17-2008", "week_16*12-18-2008*12-24-2008", "week_17*12-25-2008*12-31-2008", "week_1*09-10-2009*09-16-2009", "week_2*09-17-2009*09-23-2009", "week_3*09-24-2009*09-30-2009", "week_4*10-01-2009*10-07-2009", "week_5*10-08-2009*10-14-2009", "week_6*10-15-2009*10-21-2009", "week_7*10-22-2009*10-28-2009", "week_8*10-29-2009*11-04-2009", "week_9*11-05-2009*11-11-2009", "week_10*11-12-2009*11-18-2009", "week_11*11-19-2009*11-25-2009", "week_12*11-26-2009*12-02-2009", "week_13*12-03-2009*12-09-2009", "week_14*12-10-2009*12-16-2009", "week_15*12-17-2009*12-23-2009", "week_16*12-24-2009*12-30-2009", "week_17*12-31-2009*01-06-2010", "week_1*09-09-2010*09-15-2010", "week_2*09-16-2010*09-22-2010", "week_3*09-23-2010*09-29-2010", "week_4*09-30-2010*10-06-2010", "week_5*10-07-2010*10-13-2010", "week_6*10-14-2010*10-20-2010", "week_7*10-21-2010*10-27-2010", "week_8*10-28-2010*11-03-2010", "week_9*11-04-2010*11-10-2010", "week_10*11-11-2010*11-17-2010", "week_11*11-18-2010*11-24-2010", "week_12*11-25-2010*12-01-2010", "week_13*12-02-2010*12-08-2010", "week_14*12-09-2010*12-15-2010", "week_15*12-16-2010*12-22-2010", "week_16*12-23-2010*12-29-2010", "week_17*12-30-2010*01-05-2011", "week_1*09-11-2011*09-17-2011", "week_2*09-18-2011*09-24-2011", "week_3*09-25-2011*10-01-2011", "week_4*10-02-2011*10-08-2011", "week_5*10-09-2011*10-15-2011", "week_6*10-16-2011*10-22-2011", "week_7*10-23-2011*10-29-2011", "week_8*10-30-2011*11-05-2011", "week_9*11-06-2011*11-12-2011", "week_10*11-13-2011*11-19-2011", "week_11*11-20-2011*11-26-2011", "week_12*11-27-2011*12-03-2011", "week_13*12-04-2011*12-10-2011", "week_14*12-11-2011*12-17-2011", "week_15*12-18-2011*12-24-2011", "week_16*12-25-2011*12-31-2011", "week_17*01-01-2012*01-07-2012", "week_1*09-09-2012*09-15-2012", "week_2*09-16-2012*09-22-2012", "week_3*09-23-2012*09-29-2012", "week_4*09-30-2012*10-06-2012", "week_5*10-07-2012*10-13-2012", "week_6*10-14-2012*10-20-2012", "week_7*10-21-2012*10-27-2012", "week_8*10-28-2012*11-03-2012", "week_9*11-04-2012*11-10-2012", "week_10*11-11-2012*11-17-2012", "week_11*11-18-2012*11-24-2012", "week_12*11-25-2012*12-01-2012", "week_13*12-02-2012*12-08-2012", "week_14*12-09-2012*12-15-2012", "week_15*12-16-2012*12-22-2012", "week_16*12-23-2012*12-29-2012", "week_17*12-30-2012*01-05-2013", "week_1*09-08-2013*09-14-2013", "week_2*09-15-2013*09-21-2013", "week_3*09-22-2013*09-28-2013", "week_4*09-29-2013*10-05-2013", "week_5*10-06-2013*10-12-2013", "week_6*10-13-2013*10-19-2013", "week_7*10-20-2013*10-26-2013", "week_8*10-27-2013*11-02-2013", "week_9*11-03-2013*11-09-2013", "week_10*11-10-2013*11-16-2013", "week_11*11-17-2013*11-23-2013", "week_12*11-24-2013*11-30-2013", "week_13*12-01-2013*12-07-2013", "week_14*12-08-2013*12-14-2013", "week_15*12-15-2013*12-21-2013", "week_16*12-22-2013*12-28-2013", "week_17*12-29-2013*01-04-2014", "week_1*09-07-2014*09-13-2014", "week_2*09-14-2014*09-20-2014", "week_3*09-21-2014*09-27-2014", "week_4*09-28-2014*10-04-2014", "week_5*10-05-2014*10-11-2014", "week_6*10-12-2014*10-18-2014", "week_7*10-19-2014*10-25-2014", "week_8*10-26-2014*11-01-2014", "week_9*11-02-2014*11-08-2014", "week_10*11-09-2014*11-15-2014", "week_11*11-16-2014*11-22-2014", "week_12*11-23-2014*11-29-2014", "week_13*11-30-2014*12-06-2014", "week_14*12-07-2014*12-13-2014", "week_15*12-14-2014*12-20-2014", "week_16*12-21-2014*12-27-2014", "week_17*12-28-2014*01-03-2015", "week_1*09-13-2015*09-19-2015", "week_2*09-20-2015*09-26-2015", "week_3*09-27-2015*10-03-2015", "week_4*10-04-2015*10-10-2015", "week_5*10-11-2015*10-17-2015", "week_6*10-18-2015*10-24-2015", "week_7*10-25-2015*10-31-2015", "week_8*11-01-2015*11-07-2015", "week_9*11-08-2015*11-14-2015", "week_10*11-15-2015*11-21-2015", "week_11*11-22-2015*11-28-2015", "week_12*11-29-2015*12-05-2015", "week_13*12-06-2015*12-12-2015", "week_14*12-13-2015*12-19-2015", "week_15*12-20-2015*12-26-2015", "week_16*12-27-2015*01-02-2016", "week_17*01-03-2016*01-09-2016", "week_1*09-11-2016*09-17-2016", "week_2*09-18-2016*09-24-2016", "week_3*09-25-2016*10-01-2016", "week_4*10-02-2016*10-08-2016", "week_5*10-09-2016*10-15-2016", "week_6*10-16-2016*10-22-2016", "week_7*10-23-2016*10-29-2016", "week_8*10-30-2016*11-05-2016", "week_9*11-06-2016*11-12-2016", "week_10*11-13-2016*11-19-2016", "week_11*11-20-2016*11-26-2016", "week_12*11-27-2016*12-03-2016", "week_13*12-04-2016*12-10-2016", "week_14*12-11-2016*12-17-2016", "week_15*12-18-2016*12-24-2016", "week_16*12-25-2016*12-31-2016", "week_17*01-01-2017*01-07-2017", "week_1*09-10-2017*09-16-2017", "week_2*09-17-2017*09-23-2017", "week_3*09-24-2017*09-30-2017", "week_4*10-01-2017*10-07-2017", "week_5*10-08-2017*10-14-2017", "week_6*10-15-2017*10-21-2017", "week_7*10-22-2017*10-28-2017", "week_8*10-29-2017*11-04-2017", "week_9*11-05-2017*11-11-2017", "week_10*11-12-2017*11-18-2017", "week_11*11-19-2017*11-25-2017", "week_12*11-26-2017*12-02-2017", "week_13*12-03-2017*12-09-2017", "week_14*12-10-2017*12-16-2017", "week_15*12-17-2017*12-23-2017", "week_16*12-24-2017*12-30-2017", "week_17*12-31-2017*01-06-2018", "week_1*09-09-2018*09-15-2018", "week_2*09-16-2018*09-22-2018", "week_3*09-23-2018*09-29-2018", "week_4*09-30-2018*10-06-2018", "week_5*10-07-2018*10-13-2018", "week_6*10-14-2018*10-20-2018", "week_7*10-21-2018*10-27-2018", "week_8*10-28-2018*11-03-2018", "week_9*11-04-2018*11-10-2018", "week_10*11-11-2018*11-17-2018", "week_11*11-18-2018*11-24-2018", "week_12*11-25-2018*12-01-2018", "week_13*12-02-2018*12-08-2018", "week_14*12-09-2018*12-15-2018", "week_15*12-16-2018*12-22-2018", "week_16*12-23-2018*12-29-2018", "week_17*12-30-2018*01-05-2019", "week_1*09-08-2019*09-14-2019", "week_2*09-15-2019*09-21-2019", "week_3*09-22-2019*09-28-2019", "week_4*09-29-2019*10-05-2019", "week_5*10-06-2019*10-12-2019", "week_6*10-13-2019*10-19-2019", "week_7*10-20-2019*10-26-2019", "week_8*10-27-2019*11-02-2019", "week_9*11-03-2019*11-09-2019", "week_10*11-10-2019*11-16-2019", "week_11*11-17-2019*11-23-2019", "week_12*11-24-2019*11-30-2019", "week_13*12-01-2019*12-07-2019", "week_14*12-08-2019*12-14-2019", "week_15*12-15-2019*12-21-2019", "week_16*12-22-2019*12-28-2019", "week_17*12-29-2019*01-04-2020", "week_1*09-13-2020*09-19-2020", "week_2*09-20-2020*09-26-2020", "week_3*09-27-2020*10-03-2020", "week_4*10-04-2020*10-10-2020", "week_5*10-11-2020*10-17-2020", "week_6*10-18-2020*10-24-2020", "week_7*10-25-2020*10-31-2020", "week_8*11-01-2020*11-07-2020", "week_9*11-08-2020*11-14-2020", "week_10*11-15-2020*11-21-2020", "week_11*11-22-2020*11-28-2020", "week_12*11-29-2020*12-05-2020", "week_13*12-06-2020*12-12-2020", "week_14*12-13-2020*12-19-2020", "week_15*12-20-2020*12-26-2020", "week_16*12-27-2020*01-02-2021", "week_17*01-03-2021*01-09-2021", "week_1*09-12-2021*09-18-2021", "week_2*09-19-2021*09-25-2021", "week_3*09-26-2021*10-02-2021", "week_4*10-03-2021*10-09-2021", "week_5*10-10-2021*10-16-2021", "week_6*10-17-2021*10-23-2021", "week_7*10-24-2021*10-30-2021", "week_8*10-31-2021*11-06-2021", "week_9*11-07-2021*11-13-2021", "week_10*11-14-2021*11-20-2021", "week_11*11-21-2021*11-27-2021", "week_12*11-28-2021*12-04-2021", "week_13*12-05-2021*12-11-2021", "week_14*12-12-2021*12-18-2021", "week_15*12-19-2021*12-25-2021", "week_16*12-26-2021*01-01-2022", "week_17*01-02-2022*01-08-2022", "week_1*09-11-2022*09-17-2022", "week_2*09-18-2022*09-24-2022", "week_3*09-25-2022*10-01-2022", "week_4*10-02-2022*10-08-2022", "week_5*10-09-2022*10-15-2022", "week_6*10-16-2022*10-22-2022", "week_7*10-23-2022*10-29-2022", "week_8*10-30-2022*11-05-2022", "week_9*11-06-2022*11-12-2022", "week_10*11-13-2022*11-19-2022", "week_11*11-20-2022*11-26-2022", "week_12*11-27-2022*12-03-2022", "week_13*12-04-2022*12-10-2022", "week_14*12-11-2022*12-17-2022", "week_15*12-18-2022*12-24-2022", "week_16*12-25-2022*12-31-2022", "week_17*01-01-2023*01-07-2023", "week_1*09-10-2023*09-16-2023", "week_2*09-17-2023*09-23-2023", "week_3*09-24-2023*09-30-2023", "week_4*10-01-2023*10-07-2023", "week_5*10-08-2023*10-14-2023", "week_6*10-15-2023*10-21-2023", "week_7*10-22-2023*10-28-2023", "week_8*10-29-2023*11-04-2023", "week_9*11-05-2023*11-11-2023", "week_10*11-12-2023*11-18-2023", "week_11*11-19-2023*11-25-2023", "week_12*11-26-2023*12-02-2023", "week_13*12-03-2023*12-09-2023", "week_14*12-10-2023*12-16-2023", "week_15*12-17-2023*12-23-2023", "week_16*12-24-2023*12-30-2023", "week_17*12-31-2023*01-06-2024"
    ]

# Convert the date ranges and labels into a list of tuples for comparison
date_ranges = []
for range_str in date_ranges_str:
    label, start_str, end_str = range_str.split('*')
    start_date = datetime.strptime(start_str, "%m-%d-%Y")
    end_date = datetime.strptime(end_str, "%m-%d-%Y")
    date_ranges.append((label, start_date, end_date))

# Function to find the applicable date range label for a given date
def find_date_range_label(given_date):
    for label, start_date, end_date in date_ranges:
        if start_date <= given_date <= end_date:
            return label
    return "No Label Found"

# Path to your original and new CSV files
input_csv_path = 'nfl_data2002-2019csv.csv'
output_csv_path = 'nfl_data2002-2019withweeks.csv'

# Read the original CSV and write to a new one with the additional 'Label' column
with open(input_csv_path, mode='r') as csv_file, open(output_csv_path, mode='w', newline='') as new_csv_file:
    csv_reader = csv.DictReader(csv_file)
    fieldnames = csv_reader.fieldnames + ['week']  # Add the new column name
    
    csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for row in csv_reader:
        # Parse the date from the 'Date' column
        date = row.get("date")
        given_date = datetime.strptime(date, "%m/%d/%y")
        # Find the applicable date range label
        label = find_date_range_label(given_date)
        # Add the label to the row under the 'Label' column
        row['week'] = label
        # Write the updated row to the new CSV file
        csv_writer.writerow(row)

'''import csv

# Define the path to your CSV file
csv_file_path = 'nfl_data2002-2019csv.csv'

# Open the CSV file for reading
with open(csv_file_path, mode='r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate over each row in the CSV
    for row in csv_reader:
        # Extract and print the date from the 'Date' column
        print(row['date'])'''