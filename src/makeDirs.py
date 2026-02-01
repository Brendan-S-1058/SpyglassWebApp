import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    teamFileStructureOne = 'public/data/Teams/' + str(inputS) + '/' + str(inputS) + 'Graphs'
    teamFileStructureTwo = 'public/data/Teams/' + str(inputS) + '/' + str(inputS) + 'PitScouting'

    os.makedirs (teamFileStructureOne)
    os.makedirs (teamFileStructureTwo)

    try:
        with open ("public/data/Teams/" + str(inputS) + '/' + str(inputS) + 'Public.txt', 'x') as file:
            file.close ()
    except:
        pass
Main ()