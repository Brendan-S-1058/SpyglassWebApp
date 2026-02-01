import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    teamFileStructureOne = 'public/data/Teams/' + str(inputS) + '/' + str(inputS) + 'Graphs'
    teamFileStructureTwo = 'public/data/Teams/' + str(inputS) + '/' + str(inputS) + 'PitScouting'

    count = 0

    try:
        os.makedirs (teamFileStructureOne)
        count += 1
    except:
        pass

    try:
        os.makedirs (teamFileStructureTwo)
        count += 1
    except:
        pass

    try:
        with open ("public/data/Teams/" + str(inputS) + '/' + str(inputS) + 'Public.txt', 'x') as file:
            file.close ()
        count += 1
    except:
        pass

    print (json.dumps('number of dirs made: ' + str(count)))

Main ()