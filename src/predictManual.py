import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))

    print ('inputS: ' + str(inputS), file=sys.stderr)
    print ('inputR: ' + str(inputR), file=sys.stderr)

Main ()