#Importing the packages

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import time

base_url = 'https://understat.com/match/'
match = str(input('Please Enter the Match'))
url = base_url + match

def parsing_req(url):
    time.sleep(2)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    scripts = soup.find_all('script')
    return scripts
scripts = parsing_req(url)

def parse_cleaner(scripts):
    strings = scripts[1].string
    # strip unnecessary symbols and get only JSON data
    index_start = strings.index("('")+2
    index_end = strings.index("')")
    json_data = strings[index_start:index_end]
    return json_data

json_data = parse_cleaner(scripts)

def get_json_data(json_data):

    #encoding an decoding json data
    json_data = json_data.encode('utf8').decode('unicode-escape')
    data = json.loads(json_data)
    return data
data = get_json_data(json_data)

#Creating lists to store the data
data_home = data['h']
data_away = data['a']

player = list()
x = list() #x co-ordinated
y = list() #y co-ordinated
xG = list()
result = list()
team = list()
minute = list()
shotType = list()
player_assisted = list()
situation = list()
lastAction = list()

    #appending datas to the lists we created
    #we will create two separate lists for home and away

def converting_json(data):

    #Home Data
    for index in range(len(data_home)):
        for key in data_home[index]:

            if key == 'player':
                player.append(data_home[index][key])

            if key == 'X':
                x.append(data_home[index][key])

            if key == 'Y':
                y.append(data_home[index][key])

            if key == 'xG':
                xG.append(data_home[index][key])

            if key == 'result':
                result.append(data_home[index][key])

            if key == 'h_team':
                team.append((data_home[index][key]))

            if key == 'shotType':
                shotType.append(data_home[index][key])

            if key == 'player_assisted':
                player_assisted.append(data_home[index][key])

            if key == 'situation':
                situation.append(data_home[index][key])

            if key == 'lastAction':
                lastAction.append(data_home[index][key])

            if key == 'minute':
                minute.append(data_home[index][key])

    #Away Data
    for index in range(len(data_away)):
        for key in data_away[index]:

            if key == 'player':
                player.append(data_away[index][key])

            if key == 'X':
                x.append(data_away[index][key])

            if key == 'Y':
                y.append(data_away[index][key])

            if key == 'xG':
                xG.append(data_away[index][key])

            if key == 'result':
                result.append(data_away[index][key])

            if key == 'a_team':
                team.append((data_away[index][key]))

            if key == 'shotType':
                shotType.append(data_away[index][key])

            if key == 'player_assisted':
                player_assisted.append(data_away[index][key])

            if key == 'situation':
                situation.append(data_away[index][key])

            if key == 'lastAction':
                lastAction.append(data_away[index][key])

            if key == 'minute':
                minute.append(data_away[index][key])


        col_names = ['player','player_assisted', 'result','minute','team','xG', 'shotType', 'situation', 'lastAction', 'X', 'Y']
        football_df1= pd.DataFrame([player,player_assisted,result,minute,team,xG,shotType,situation, lastAction,x,y], index=col_names)
        football_df1= football_df1.T

        return football_df1
football_df1= converting_json(data)

football_df1.to_csv('./football_stats.csv', index=False, header=True)
