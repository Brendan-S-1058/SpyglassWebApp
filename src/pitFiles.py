import sys
import json
import os
import base64

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    list = []
    hold = ''
    for char in inputS:
        if char != ',':
            hold += char
        else:
            list.append(hold)
            hold = ''
    list.append(hold)
    del hold
    
    print ('List - EARLY: ' + str(list), file=sys.stderr)
    #need to remove the prefix to the link, separated by a comma naturally, very conveinently
    list.pop(2)
    print ('List - LATE: ' + str(list), file=sys.stderr)

    image_bytes = base64.b64decode(list[2])

    print ('image_bytes: ' + str(image_bytes), file=sys.stderr)
    print ('inputS: ' + str(inputS), file=sys.stderr)

Main ()