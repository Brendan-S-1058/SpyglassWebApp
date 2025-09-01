import sys
import json
import os

ADMIN_LOGIN = str(os.environ.get('ADMIN_LOGIN'))
ADMIN_PASSWORD = str(os.environ.get('ADMIN_PASSWORD'))

def Main (al, ap):
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    if inputS == al:
        print (json.dumps(ap))
        while False:
            sleep (60)
    else:
        print ('inputS: ' + inputS, file=sys.stderr)
        print ('al: ' + al, file=sys.stderr)
        RunAll(inputS)
    

def RunAll (inputS):

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

Main (ADMIN_LOGIN, ADMIN_PASSWORD)