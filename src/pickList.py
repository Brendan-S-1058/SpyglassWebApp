import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

    print (inputI, file=sys.stderr)

    if inputI[0] == 1:
        Public ()
    else:
        Local ()

def Public ():
    with open("Public.txt","r") as f:
        rawData = file.read()
        f.close()
    qqq = SortAndReturn (rawData)
    

def Local ():
    print ("Local mode does not exist yet", file=sys.stderr)

def SortAndReturn ():
    return null 

'''
1: figure out input
2: figure out intended output
3: make a structure to convert input to output in both cases
'''

Main ()