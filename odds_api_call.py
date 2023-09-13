import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ODDS_API_KEY')

SPORT = "americanfootball_nfl"
MARKET = "h2h&odds"
REGION = "us"
ODDS_FORMAT = "american"

#example
response = requests.get(f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?regions={REGION}&markets={MARKET}Format=american&apiKey={API_KEY}")

if response.status_code != 200:
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')
else:
    print ('List of NFL games:',
    response.json())