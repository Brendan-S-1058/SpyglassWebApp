import sys
import json

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

    with open ("public/data/testData.txt", 'w') as file:
        file.write (team + '/' + passw + ',')
        file.close ()
    
    print (json.dumps("newpassword: " + str(passw)))

Main ()