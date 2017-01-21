"""
Soccer Scheduling
"""

import http.client
import datetime
import json
from teams import *

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'a49c78a50c0e486ca40791f1c9323b12', \
           'X-Response-Control': 'minified' }

def find_team(team_name, teams_dict):
    
    #check the master dictionary for the input team name
    for item in teams_dict['teams']:
        #if found return that teams id
        if team_name.lower() in item['name'].lower():
            return item['id']
    
    return 0

def get_schedule(time_int, n_p_bool, team):
    
    #decide if the time frame is future(true) or past(false)
    if n_p_bool:
        t_f_str = "n" #future
    else:
        t_f_str = "p" #past
    
    #build path of which fixtures to get
    path_str = "/v1/teams/" + str(team) + "/fixtures?timeFrame=" \
                + t_f_str + str(time_int)
    
    
    connection.request('GET', path_str, None, headers )
    response2 = json.loads(connection.getresponse().read().decode())
    
    return response2

def parse_output(team_schedule):
    
    games_list = list()    
    
    for item in team_schedule['fixtures']:
        game_time = item['date']
        
        year_str = game_time[0:4]
        year_int = int(year_str)
        
        month_str = game_time[5:7]
        month_int = int(month_str)
        
        day_str = game_time[8:10]
        day_int = int(day_str)
        
        time_str = game_time[11:-1]
        hour_int = int(time_str[0:2])
        minute_int = int(time_str[3:5])
        second_int = int(time_str[6:])
        
        print(time_str + ' ' + month_str + ' ' + day_str + ' ' + year_str)
        print()
        
        game_time_tup = \
            (year_int, month_int, day_int, hour_int, minute_int, second_int)
        
        games_list.append(game_time_tup)
    
    return games_list


#print(response2["fixtures"][0]["awayTeamId"])

input_str = input("team: ")

team_id_int = find_team(input_str, teams_dict)

team_schedule = get_schedule(14, True, team_id_int)

fixture_time_list = parse_output(team_schedule)

now = datetime.datetime.now()

for item in fixture_time_list:
    print(item)


#print (response2)
