from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

#sunday dict for week1s_to_all_search_inputs
week_1_sundays = {2000: "09-03-2000", 2001: "09-09-2001", 2002: "09-05-2002", 2003: "09-04-2003", 2004: "09-09-2004", 2005: "09-08-2005", 2006: "09-07-2006", 2007: "09-06-2007", 2008: "09-04-2008", 2009: "09-10-2009", 2010: "09-09-2010", 2011: "09-11-2011", 2012: "09-09-2012", 2013: "09-08-2013", 2014: "09-07-2014", 2015: "09-13-2015", 2016: "09-11-2016", 2017: "09-10-2017", 2018: "09-09-2018", 2019: "09-08-2019", 2020: "09-13-2020", 2021: "09-12-2021", 2022: "09-11-2022", 2023: "09-10-2023"}

# takes dict of week 1 sunday and returns all relevant date ranges for power rankings #

def week1s_to_all_search_inputs(week_1_date_dict):
    week_1_sundays = week_1_date_dict
    all_weeks = []
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
    return list(reversed(all_weeks))

# takes week, date from, date till info from week1s_to_all_search_inputs and creates string for google_api.py #
# from google_api_inputs2 import adjusted_week_1_reversed as week_list

def query_builder(week_list):
    concat_search_phrase_list = []
    for item in week_list:
        input_list = item.split("*")
        week = input_list[0]
        search_body = "nfl " + week + " power rankings"
        after_date = "after:" + input_list[1]
        before_date = "before:" + input_list[2]
        current_website = "espn.com"
        site_info = "site:" + current_website
        concat_search_phrase = search_body + " " + site_info + " " + after_date + " " + before_date + " "
        concat_search_phrase_list.append(concat_search_phrase)

    return concat_search_phrase_list

step1 = week1s_to_all_search_inputs(week_1_sundays)
print(query_builder(step1))