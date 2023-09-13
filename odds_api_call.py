import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ODDS_API_KEY')

#example
response = requests.get(f"https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=american&apiKey={API_KEY}")

print(response)