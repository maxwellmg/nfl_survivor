from googleapiclient.discovery import build
#import pprint
import os
#import requests
from dotenv import load_dotenv
from google_api_inputs import season_week_list

for item in season_week_list:
    week_list = item.split("*")
    season = week_list[0]
    week = week_list[1]
    print("season: " + str(season))
    print("week: " + str(week))
'''
load_dotenv()

my_api_key = os.getenv('GOOGLE_API_KEY')
my_cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')

dev_key = os.getenv('GOOGLE_API_KEY')
my_cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')

def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('espn power rankings 2023 week 3', my_cse_id, num=1)
for result in results:
    print(result.get('link'))'''