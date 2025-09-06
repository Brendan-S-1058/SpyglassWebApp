import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    escaped = False
    hold = ''
    purpose = ''
    for char in inputS:
        if escaped == True:
            hold += char
        else:
            if char == '⌧':
                escaped == True
            else:
                purpose += char
    
    if purpose == 'write':
        Write (hold)
    else:
        Read ()

def Read ():

    FinalSave = ''
    
    with open ("public/data/testData.txt", 'r') as file:
        oldSecrets = file.read()
        file.close ()
    
    FinalSave += oldSecrets + '⇯'

    holdTeam = ''
    teamList = []
    for char in oldSecrets:
        if char != '/' and char != ',':
            holdTeam += char
        else:
            if char == '/':
                teamList.append(holdTeam)
            holdTeam = ''
    
    for team in holdTeam:
        with open ("public/data/Teams/" + str(team) + '/' + str(team) + 'Public.txt', 'r') as file:
            teamData = file.read ()
            file.close ()
        
        FinalSave += team + 'ɀ̣' + teamData + '⸮'
    
    print (json.dumps(FinalSave))

    
def Write (secrets):

    holdTeam = ''
    teamList = []
    for char in secrets:
        if char != '/' and char != ',':
            holdTeam += char
        else:
            if char == '/':
                teamList.append(holdTeam)
            holdTeam = ''
    
    for team in teamList:
        teamFileStructure = 'public/data/Teams/' + str(team) + '/' + str(team) + 'Graphs'
        os.makedirs (teamFileStructure)
        
        with open ("public/data/Teams/" + str(team) + '/' + str(team) + 'Public.txt', 'x') as file:
            file.close ()
    
    with open ("public/data/testData.txt", 'w') as file:
        file.write (secrets)
        file.close ()

    print (json.dumps('nothing'))



Main ()