import requests
import sys
import json
import os

inputR = sys.stdin.read()
keys = json.loads(inputR)


TEAM_KEY = ''
EVENT_KEY = ''
one = True
for char in keys:
    if char != ',':
        if one == True:
            TEAM_KEY += char
        else:
            EVENT_KEY += char
    else:
        one = False

API_KEY = os.environ.get('TBA_API_KEY')

BASE_URL = "https://www.thebluealliance.com/api/v3"

headers = {
    "X-TBA-Auth-Key": API_KEY
}

matches_url = BASE_URL + "/team/frc" + TEAM_KEY + "/event/" + EVENT_KEY + "/matches"
matches_response = requests.get(matches_url, headers=headers)
matches_data = matches_response.json()

print ("matches_data: " + str(matches_data), file=sys.stderr)

matches = []
for match in matches_data:
    one = []
    for blueTeam in match['alliances']['blue']['team_keys']:
        one.append(blueTeam)
    for redTeam in match['alliances']['red']['team_keys']:
        one.append (redTeam)
    matches.append(one)

print ('matches: '+ str(matches), file=sys.stderr)

newMatches = []
for match in matches:
    newMatch = []
    for team in match:
        holdTeam = ''
        for char in team:
            if char in '1234567890':
                holdTeam += char
        print ('holdteam: ' + str(holdTeam), file=sys.stderr)
        newMatch.append (int(holdTeam))
    newMatches.append (newMatch)

print ('newmatches: '+ str(newMatches), file=sys.stderr)

print (json.dumps(newMatches))