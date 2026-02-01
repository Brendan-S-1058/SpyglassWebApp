import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    print ('inputR: ' + str(inputR), file=sys.stderr)
    print ('inputS: ' + str(inputS), file=sys.stderr)

Main ()