import requests
from bs4 import BeautifulSoup
import pandas as pd


result = requests.get("https://www.espn.com/nhl/matchup/_/gameId/401145658")
src = result.content

soup = BeautifulSoup(src, 'html.parser')

team1 = ""
team2 = ""
count = 0

for row in soup.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]

    if count > 14:
        break
    print(row_text)

    if count == 0:
        team1Name = ''.join(row_text[0])

    elif count == 1:
        #uhhhh
        team2Name = ''.join(row_text[0])


    elif count >=2:
        team1 = team1 + ";" + ''.join(row_text[1])
        team2 = team2 + ";" + ''.join(row_text[2])

    count = count + 1


team1 = (team1Name + team1)
team2 = (team2Name + team2)

row1 = team1.split(";")
row2 = team2.split(";")


columns = ['Team', 'Shots', 'Hits', 'Faceoffs_Won', 'Faceoff_Win_Percent', 'Power_Play_Opportunities',
                      'Power_Play_Goals', 'Power_Play_Percentage', 'Shot_Handed_Goals', 'Total_Penalties',
                      'Penalty_Minutes', 'Blocked_Shots', 'Takeaways', 'Giveaways']


df = pd.DataFrame(row1)
df = df.transpose()
df.columns = columns
to_append = row2
df_length = len(df)
df.loc[df_length] = to_append

df.to_csv('NHL_DataBase.csv', index=False)




