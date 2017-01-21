"""
Soccer Scheduling
"""

import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'a49c78a50c0e486ca40791f1c9323b12', 'X-Response-Control': 'minified' }

def get_schedule(time_int, n_p_bool, team):
    #connection.request('GET', '/v1/competitions', None, headers )
    #response = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/teams/66/fixtures?timeFrame=n14', None, headers )
    response2 = json.loads(connection.getresponse().read().decode())
    
    return response2

#print(response2["fixtures"][0]["awayTeamId"])

response2 = get_schedule(1,1,1)

print (response2)
