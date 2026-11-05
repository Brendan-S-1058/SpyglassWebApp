import sys
import json

def Main ():
    inputR = sys.stdin.read()
    team = json.loads(inputR)

    print ('team:' + str(team), file=sys.stderr)

    with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(team) + 'TeamsScouted.txt', 'r') as file:
        rawData = file.read ()
        file.close ()

    print ('data: ' + str(rawData), file=sys.stderr)
    print (json.dumps(rawData))

Main()