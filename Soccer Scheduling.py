"""
Soccer Scheduling
"""

import http.client
import json
from teams import *

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'a49c78a50c0e486ca40791f1c9323b12', \
           'X-Response-Control': 'minified' }

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

response2 = get_schedule(14, True, 66)

print(response2["fixtures"][0]["awayTeamId"])

#print (response2)
