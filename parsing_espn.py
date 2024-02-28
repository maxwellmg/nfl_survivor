from bs4 import BeautifulSoup
import requests
import json

#import scrapy

#url = 'https://www.espn.com/nfl/story/_/id/38727212/nfl-week-8-power-rankings-poll-2023-plus-every-team-young-riser'
#url = 'https://www.buzzfeed.com/meganeliscomb/things-to-stop-putting-on-your-resume?d_id=4878097&ref=bftwbuzzfeed&utm_source=dynamic&utm_campaign=bftwbuzzfeed'
#r = requests.get(url)

sample_dict_final = {"nfl week 11 power rankings site:espn.com after:2017-11-12 before:2017-11-16 ": "https://www.espn.com/nfl/story/_/page/NFLpowerrankingsx171114/nfl-2017-week-11-power-rankings-win-projections-all-32-teams-new-orleans-saints-join-philadelphia-eagles-new-england-patriots-top"}

# Loop will parse each query for week and season information before requesting data from espn, where it will record a unique set of data for each team (week, season, ranking, team) before appending to a JSON file

for query, url in sample_dict_final.items():
    parsing = query.split(" ")
    week = parsing[2]
    season = parsing[6].split(":")[1].split("-")[0]
    month = parsing[6].split(":")[1].split("-")[1]
    if month == "01":
        season = str(int(season) - 1)
    try:

        with open("sample_html_2017.html") as fp:
            soup = BeautifulSoup(fp, 'html5lib')
        fp.close()

        '''r = requests.get(url)
        r.raise_for_status() # This will throw an exception if status is 4xx or 5xx

        soup = BeautifulSoup(r.content, 'html5lib')'''
        
        # Open JSON, Download Content Locally as 'data', Close File #

        with open("espn_data.json") as f:
            data = json.load(f)
        f.close()

        # Parse Soup for Teams and Power Rankings #

        for tag in soup.find_all('h2'):
            if len(tag.text) < 30:
                if "." in tag.text:
                    if " " in tag.text:
                        power_ranking = tag.text.split(" ")[0].replace(".", "")
                        team = " ".join(tag.text.split(" ")[1:])

                        # Create new JSON data, append to data #

                        new_data = {'season': season, 'week': week, 'team': team, 'power_ranking': power_ranking}
                        data.append(new_data)

        with open("espn_data.json", "w") as f:
            json.dump(data, f)
        f.close()

    except requests.HTTPError as e:
        print('Error', e)
        #return None
    except requests.exceptions.RequestException as e:
        print("Connection refused", e)
        #return None
    except Exception as e:
        print("Internal error", e)
        #return None
    

    

'''
# Sample Code that Works with HTML File #
    with open("sample_html_2017.html") as fp:
        soup = BeautifulSoup(fp, 'html5lib')
    fp.close()

    for tag in soup.find_all('h2'):
        if len(tag.text) < 30:
            if "." in tag.text:
                if " " in tag.text:
                    ranking = tag.text.split(" ")[0].replace(".", "")
                    team = " ".join(tag.text.split(" ")[1:])
                    #print(ranking)
                    #print(team)

'''





