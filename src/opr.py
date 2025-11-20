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
    count = 1
    for char in match: 
        if char == ',' and count != 1:
            holderList.append(hold)
            hold = ''
        elif char != ',':
            hold += char
        count += 1 
    holderList.append(hold)
    hold = ''
    holdestList.append(holderList)
    holderList = []

print ('holdestList1: ' + str(holdestList), file=sys.stderr)

for match in holdestList:
    match.pop(len(match)-1)

print ('holdestList2: ' + str(holdestList), file=sys.stderr)

for match in holdestList:
    for i in range(len(match)):
        match[i] = int(match[i])

sortedData = holdestList
print ('sortedData: ' + str(sortedData), file=sys.stderr)

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