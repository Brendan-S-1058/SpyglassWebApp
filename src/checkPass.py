import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    print (inputS, file=sys.stderr)

    with open('public/data/testData.txt', 'r') as file:
        allData = file.read()
        file.close
    
    hold = ''
    teams = []
    passwords = [] 
    for char in allData:
        if char != ',' and char != '/':
            hold += char
        elif char == ',':
            passwords.append(hold)
            hold = ''
        else:
            teams.append (hold)
            hold = ''
    
    teamPresent = False
    for i in range (len(teams)):
        if teams[i] == inputS:
            teamPresent = True
            drowssap = passwords[i]
    
    if teamPresent == True:
        print (json.dumps(drowssap))
    else:
        print (json.dumps(teamPresent))

Main ()