import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    team = ''
    inquireTeam = ''
    comma = False
    for char in inputS:
        if char == ',':
            comma = True
        elif not comma:
            team += char
        else:
            inquireTeam += char
    
    with open ('public/data/Teams/' + team + '/' + team + 'PitScouting/' + inquireTeam + 'Data.txt', 'r') as file:
        currentData = file.read()

    print ('currentData: ' + currentData, file = sys.stderr)

    print (json.dumps(currentData))

Main ()