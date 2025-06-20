import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = int(json.loads(inputR))
    if inputI == '1':
        Public ()
    else:
        Local ()

def Public ():
    with open("Public.txt","r") as f:
        rawData = file.read()
        f.close()
    SortAndReturn (rawData)
    

def Local ():
    print ("Local mode does not exist yet", file=sys.stderr)

def SortAndReturn ():
    return null 

Main ()