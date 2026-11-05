import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    teams = []
    heldTeam = ''
    for char in inputS:
        if char == ',':
            teams.append(heldTeam)
            heldTeam = ''
        else:
            heldTeam += char

    with open ('public/data/Teams/' + str(teams[0]) + '/' + str(teams[0]) + 'comps.txt', 'a') as file:
        file.write(str(teams[1]) + ',' + str(teams[2]) + ',0/')
        file.close ()

    json.dumps("hey it didn't crash :)")

Main()