import sys
import json
import os

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    print ('inputS: ' + str(inputS), file=sys.stderr)

Main ()