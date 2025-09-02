import sys
import json
import os

ADMIN_LOGIN = str(os.environ.get('ADMIN_USER'))
ADMIN_PASSWORD = str(os.environ.get('ADMIN_PASSWORD'))

API_KEY = os.environ.get('TBA_API_KEY')

def Main (al, ap):
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    if inputS == al:
        print (json.dumps(ap + ',yes'))
    else:
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
        print (json.dumps(drowssap + ',no'))
    else:
        print (json.dumps(teamPresent + ',no'))

Main (ADMIN_LOGIN, ADMIN_PASSWORD)