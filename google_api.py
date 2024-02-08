from googleapiclient.discovery import build
import pprint
import os
#import requests
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv('GOOGLE_API_KEY')
my_cse_id = os.getenv('CUSTOM_SEARCH_ENGINE_ID')

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'stackoverflow site:en.wikipedia.org', my_api_key, my_cse_id, num=1)
for result in results:
    pprint.pprint(result)