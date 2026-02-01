import sys
import json
import os
import base64

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    list = []
    hold = ''
    for char in inputS:
        if char != ',':
            hold += char
        else:
            list.append(hold)
            hold = ''
    list.append(hold)
    del hold
    
    print ('List - EARLY: ' + str(list), file=sys.stderr)
    #need to remove the prefix to the link, separated by a comma naturally, very conveinently
    list.pop(3)
    print ('List - LATE: ' + str(list), file=sys.stderr)

    image_bytes = base64.b64decode(list[3])
    team = list[1]
    scoutedTeam = list[0]
    scoutedData = list[2]

    del list

    print ('image_bytes: ' + str(image_bytes), file=sys.stderr)
    print ('inputS: ' + str(inputS), file=sys.stderr)

    try:
        with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(scoutedTeam) + 'Picture.png', 'x') as file:
            file.close()
    except:
        pass

    with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(scoutedTeam) + 'Picture.png', 'wb') as file:
        file.write(image_bytes)
    
    try:
        with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(scoutedTeam) + 'Picture.png', 'r') as file:
            held = file.read()
    except: 
        held = ''
    
    hold = ''
    list = []
    for char in held:
        if char != ',':
            hold+=char
        else:
            list.append(hold)
            hold = ''
    
    if str(scoutedTeam) not in list:
        with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(scoutedTeam) + 'Picture.png', 'a') as file:
            file.write(str(scoutedTeam) + ',')
    
    with open ('public/data/Teams/' + str(team) + '/' + str(team) + 'PitScouting/' + str(scoutedTeam) + 'Picture.png', 'w') as f:
        file.write (scoutedData)
    
    print(json.dumps('yay, no errors'))
Main ()