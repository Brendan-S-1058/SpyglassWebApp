import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))

    print ('inputS: ' + str(inputS), file=sys.stderr)
    print ('inputR: ' + str(inputR), file=sys.stderr)

    teams = [inputS[0], inputS[1], inputS[2], inputS[3], inputS[4], inputS[5]]
    data = inputS[6]

    print (teams, file = sys.stderr)
    print (data, file = sys.stderr)

Main ()