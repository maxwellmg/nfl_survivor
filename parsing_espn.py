from bs4 import BeautifulSoup
#import requests
#import scrapy

#url = 'https://www.espn.com/nfl/story/_/id/38727212/nfl-week-8-power-rankings-poll-2023-plus-every-team-young-riser'
#url = 'https://www.buzzfeed.com/meganeliscomb/things-to-stop-putting-on-your-resume?d_id=4878097&ref=bftwbuzzfeed&utm_source=dynamic&utm_campaign=bftwbuzzfeed'
#r = requests.get(url)

#response = r.css("h2").getall()
#response = response.css("h2").getall()
#with open("response_h2_output.txt")


#soup = BeautifulSoup(r.content, 'html5lib')
with open("sample_html_2022.html") as fp:
    soup = BeautifulSoup(fp, 'html5lib')
fp.close()

#print(soup.prettify())
for tag in soup.find_all('h2'):
    if len(tag.text) < 30:
        if "." in tag.text:
            if " " in tag.text:
                ranking = tag.text.split(" ")[0]
                team = " ".join(tag.text.split(" ")[1:])
                print(ranking)
                print(team)
'''h2s = soup.find_all('h2')
print(h2s)'''
#print(soup.text)
#print(soup.prettify())
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(len("Washington Football Team"))

