import requests
import sys
import json
import os

inputR = sys.stdin.read()
EVENT_KEY = json.loads(inputR)

API_KEY = os.environ.get('TBA_API_KEY')

BASE_URL = "https://www.thebluealliance.com/api/v3"

headers = {
    "X-TBA-Auth-Key": API_KEY
}

teams_url = BASE_URL + '/event/' + EVENT_KEY + '/teams'
teams_response = requests.get(teams_url, headers=headers)
teams_data = teams_response.json()

teamList = []

print ('teams_data: ' + str(teams_data), file=sys.stderr)

for team in teams_data:
    teamList.append(team['team_number'])

matches_url = BASE_URL + '/event/' + EVENT_KEY + '/matches'
matches_response = requests.get(matches_url, headers=headers)
matches_data = matches_response.json()

matchList = []
matchNumbers = []

for matchNum in matches_data:
    matchNumbers.append (matchNum['key'])

holdList = []
for key in (matchNumbers):
    hold = ''
    fullHold = ''
    post = False
    for char in key:
        if post == True:
            if char in '1234567890':
                hold += char
            else:
                fullHold += char
        if char == '_':
            post = True
    holdList.append(fullHold + hold)
matchNumbers = holdList

del holdList
del hold
del fullHold

for matchKey in matches_data:
    matchList.append (matchKey['alliances']['blue']['team_keys'] + matchKey['alliances']['red']['team_keys'])

TeamsByMatch = {}
for i in range (len(matchNumbers)):
    TeamsByMatch[matchNumbers[i]] = matchList[i]

holdKey = ''
holdKeyList1 = []
holdKeyList2 = []
holdKeyList3 = []
for i in range(len(matchNumbers)):
    if 'f' not in matchNumbers[i]:
        holdKeyList1.append(matchNumbers[i])
    elif 's' in matchNumbers[i]:
        holdKeyList2.append(matchNumbers[i])
    else:
        holdKeyList3.append(matchNumbers[i])

holdList = []
for key in holdKeyList1:
    hold = ''
    for char in key:
        if char in '1234567890':
            hold += char
    holdList.append(int(hold))
holdList.sort ()
sortedHoldList = []
for key in holdList:
    sortedHoldList.append('qm' + str(key))
holdKeyList1 = sortedHoldList

holdList = []
for key in holdKeyList2:
    hold = ''
    for char in key:
        if char in '1234567890':
            hold += char
    holdList.append(int(hold))
holdList.sort ()
sortedHoldList = []
for key in holdList:
    sortedHoldList.append('sfm' + str(key))
holdKeyList2 = sortedHoldList

holdList = []
for key in holdKeyList3:
    hold = ''
    for char in key:
        if char in '1234567890':
            hold += char
    holdList.append(int(hold))
holdList.sort ()
sortedHoldList = []
for key in holdList:
    sortedHoldList.append('fm' + str(key))
holdKeyList3 = sortedHoldList

del holdList
del hold
del sortedHoldList
del holdKey

matchNumbers = holdKeyList1 + holdKeyList2 + holdKeyList3

orderedMatchList = []
for i in range (len(matchNumbers)):
    orderedMatchList.append(TeamsByMatch[matchNumbers[i]])

holdMatches = []
for match in orderedMatchList:
    holdTrueTeams = []
    for team in match:
        trueTeam = ''
        for char in team:
            if char in '1234567890':
                trueTeam += char
        holdTrueTeams.append(int(trueTeam))
    holdMatches.append(holdTrueTeams)
orderedMatchList = holdMatches
del holdMatches
del trueTeam
del holdTrueTeams

print (json.dumps(orderedMatchList))