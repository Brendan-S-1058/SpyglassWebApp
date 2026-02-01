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

Main ()