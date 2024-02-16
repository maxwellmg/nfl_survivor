from googleapiclient.discovery import build
import os
#import requests
from dotenv import load_dotenv
from function_library import week_1_sundays, week1s_to_all_search_inputs, query_builder
import json

step1 = week1s_to_all_search_inputs(week_1_sundays)
concat_search_phrase_list = (query_builder(step1))

load_dotenv()
'''
my_api_key = os.getenv('GOOGLE_API_KEY')
my_cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')'''

dev_key = os.getenv('GOOGLE_API_KEY')
my_cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')

def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

power_rankings = {}

for search_phrase in concat_search_phrase_list:
    try:
        results = google_search(search_phrase, my_cse_id, num=1)
        for result in results:
            first_link = result.get('link')
            power_rankings.update({search_phrase: first_link})
            print({search_phrase: first_link})
    except:
        with open("power_rankings.json") as f:
            data = json.load(f)
            data.append(power_rankings)
        with open("power_rankings.json", "w") as f:
            json.dump(data, f)
        f.close()