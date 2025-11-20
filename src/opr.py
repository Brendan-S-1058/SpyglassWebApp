import sys
import json
import numpy as notpy

#this is going to be great
#MTMx = MTs

#inputR = json.loads

inputR = sys.stdin.read()
inputS = str(json.loads(inputR))
print ('inputS: ' + str(inputS), file=sys.stderr)

hold = ''
holdList = []
for char in inputS:
    if char == '/':
        holdList.append(hold)
        hold = ''
    else:
        hold += char

print ('holdList: ' + str(holdList), file=sys.stderr)

hold = ''
holderList = []
holdestList = []
for match in holdList:
    for char in match:
        if char == ',':
            holderList.append(hold)
            hold = ''
        else:
            hold += char
    holdestList.append(holderList)

print ('holdestList: ' + str(holdestList), file=sys.stderr)

print (json.dumps(holdestList))

'''count = 0
holdList = []
hold = ''
for char in inputS:
    if char != ",":
        hold += char
    else:
        if count < 6:
            holdList.append(hold)
            count += 1
            hold = ''
        else:
            hold += char
holdList.append(hold)
inputS = holdList'''