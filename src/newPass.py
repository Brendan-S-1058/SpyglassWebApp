import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    print ('inputS: ' + str(inputS), file=sys.stderr)

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
    
    print ('team: ' + team, file=sys.stderr)
    print ('passw: ' + passw, file=sys.stderr)

    with open ("public/data/testData.txt", 'w') as file:
        file.write (team + '/' + passw + ',')
        file.close ()
    
    print (json.dumps("newpassword: " + str(passw)))

Main ()