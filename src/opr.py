import sys
import json
import numpy as notpy

#this is going to be great
#MTMx = MTs

#inputR = json.loads

inputR = sys.stdin.read()
inputS = str(json.loads(inputR))
print ('inputS: ' + str(inputS), file=sys.stderr)

for i in inputS:
    print ('i: ' + str(i), file=sys.stderr)

print (json.dumps(inputS))

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