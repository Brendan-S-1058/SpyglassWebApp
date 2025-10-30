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

matchNumbers = []
matchList = []

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


holdKey = ''
unsortedDict = {}
unsortedHoldKeyList = []
holdKeyList1 = []
holdKeyList2 = []
holdKeyList3 = []
for i in range(len(matchNumbers)):
    unsortedHoldKeyList.append(matchNumbers[i])
    if 'f' not in matchNumbers[i]:
        holdKeyList1.append(matchNumbers[i])
    elif 's' in matchNumbers[i]:
        holdKeyList2.append(matchNumbers[i])
    else:
        holdKeyList3.append(matchNumbers[i])

holdList = []
for key in unsortedHoldKeyList:
    hold = ''
    for char in key:
        if char in '1234567890':
            hold += char
    holdList.append(int(hold))
processedUnsortedKeyList = holdList

for i in range(len(processedUnsortedKeyList)):
    print ('processedUnsortedKeyList[i]: ' + str(processedUnsortedKeyList[i]), file=sys.stderr)
    unsortedDict[processedUnsortedKeyList[i]] = newMatches[i]

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

holdList = []
for key in matchNumbers:
    hold = ''
    for char in key:
        if char in '1234567890':
            hold += char
    holdList.append(int(hold))
cleaned = holdList

initalOrderedMatchlist = []
for key in cleaned:
    print ('key: ' + key)
    initalOrderedMatchlist.append(unsortedDict[key])

orderedMatchList = []
for i in range (len(matchNumbers)):
    orderedMatchList.append(TeamsByMatch[matchNumbers[i]])

holdMatches = []
for match in initalOrderedMatchlist:
    holdTrueTeams = []
    for team in match:
        trueTeam = ''
        for char in team:
            if char in '1234567890':
                trueTeam += char
        holdTrueTeams.append(int(trueTeam))
    holdMatches.append(holdTrueTeams)
initalOrderedMatchlist = holdMatches
del holdMatches
del trueTeam
del holdTrueTeams

print (json.dumps([initalOrderedMatchlist, matchNumbers]))