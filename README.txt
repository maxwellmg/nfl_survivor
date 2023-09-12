The following repo is meant as an exercise to:
    a. learn more about Ruby and cement existing knowledge
    b. aid in the upcoming NFL season to (hopefully) win a few survivor pools
    c. have fun

A survivor pool consists of a group of people who make one selection per week on which team in the NFL they think will win. If that team succeeds, the person who selected them remains "alive" in the pool. They must select another team the following week so long as they do not select a team they have already chosen. The last person who has not lost in the pool wins the pot.

This project is designed to provide the best mathematical chance of success. Odds are projected out for every game of the season in advance. Hopefully, it will be enough to simply factor three variables: 
    1. odds
    2. home/away
    3. Favor earlier matchups

The plan is to scrape the odds each week (with Python) for up to date data, and rerun the Ruby program with said data to chart a course through the season.

(9/12/23) I have made the repo public, happy hunting. Also it turns out it's not reflected on GitHub when you make private commits. So thats fun. :/

Betting odds: https://www.rotowire.com/betting/nfl/odds/week-18

alt betting odds: https://sportsbook.draftkings.com/nfl-odds-week-3

virtualenv for spidering: "scrapytsg"