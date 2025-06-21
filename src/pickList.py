import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

    print ("picklist input: " + str(inputI), file=sys.stderr)
'''
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
'''
1: figure out input - (-1,,1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/,100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/) or (1)
2: figure out intended output
3: make a structure to convert input to output in both cases
'''

Main ()

print (json.dumps("NOT DONE YET"))