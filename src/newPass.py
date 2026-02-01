import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    comma = False
    team = ''
    passw = ''
    for char in inputS:
        if char != ',':
            if comma == False:
                team += char
            else:
                passw += char
        else:
            if comma == False:
                comma = True
            else:
                passw += char

    with open ("public/data/testData.txt", 'a') as file:
        file.write (team + '/' + passw + ',')
        file.close ()

    teamFileStructureOne = 'public/data/Teams/' + str(team) + '/' + str(team) + 'Graphs'
    teamFileStructureTwo = 'public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting'

    os.makedirs (teamFileStructureOne)
    os.makedirs (teamFileStructureTwo)

    
    with open ("public/data/Teams/" + str(team) + '/' + str(team) + 'Public.txt', 'x') as file:
        file.close ()
    
    print (json.dumps("newpassword: " + str(passw)))

Main ()