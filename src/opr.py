import sys
import json
import numpy as np

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

matchsInData = []
for smatch in sortedData:
    if smatch[0] not in matchsInData:
        matchsInData.append(smatch[0])

teamsInData = []
for smatch in sortedData:
    if smatch[1] not in teamsInData:
        teamsInData.append(smatch[1])

alliancesByMatch = {}
for match in matchsInData:
    count = 0
    for smatch in sortedData:
        if match == smatch[0]:
            totalScore = (((smatch[2])*3)+((smatch[3])*3)+((smatch[4])*4)+((smatch[5])*6)+((smatch[6])*7)+((smatch[7])*6)+((smatch[8])*4)+((smatch[9])*2)+((smatch[10])*3)+((smatch[11])*4)+((smatch[12])*5)+((smatch[13])*6)+((smatch[14])*4)+((smatch[15])*2)+((smatch[16])*6)+((smatch[17])*12))
            #TODO: ADD REAL ALLIANCE SEPARATIONS WITH NEW INPUT PAGE
            if count == 0:
                alliancesByMatch[str(match) + 'team' + 'b'] = [smatch[1]]
                alliancesByMatch[str(match) + 'score' + 'b'] = totalScore
            elif count < 3:
                alliancesByMatch[str(match) + 'team' + 'b'].append(smatch[1])
                alliancesByMatch[str(match) + 'score' + 'b'] += totalScore
            elif count == 3:
                alliancesByMatch[str(match) + 'team' + 'r'] = [smatch[1]]
                alliancesByMatch[str(match) + 'score' + 'r'] = totalScore
            elif count < 6:
                alliancesByMatch[str(match) + 'team' + 'r'].append(smatch[1])
                alliancesByMatch[str(match) + 'score' + 'r'] += totalScore
            count += 1

print ('alliancesByMatch: ' + str(alliancesByMatch), file=sys.stderr)

teamsMatrixPre = []
scoresMatrixPre = []
for match in matchsInData:
    holdListT = []
    onAlliance = 0
    for i in range(len(teamsInData)):
        if teamsInData[i] in alliancesByMatch[str(match)+'team'+'b']:
            holdListT.append(1)
            onAlliance += 1
        else:
            holdListT.append(0)
    if onAlliance == 3:
        teamsMatrixPre.append(holdListT)
        scoresMatrixPre.append([alliancesByMatch[str(match)+'team'+'b']])
    holdListT = []
    onAlliance = 0
    for i in range(len(teamsInData)):
        if teamsInData[i] in alliancesByMatch[str(match)+'team'+'r']:
            holdListT.append(1)
            onAlliance += 1
        else:
            holdListT.append(0)
    if onAlliance == 3:
        teamsMatrixPre.append(holdListT)
        scoresMatrixPre.append([alliancesByMatch[str(match)+'team'+'r']])

print ('teamsMatrixPre: ' + str(teamsMatrixPre), file=sys.stderr)
print ('scoresMatrixPre: ' + str(scoresMatrixPre), file=sys.stderr)


teamsMatrix = np.array(teamsMatrixPre)
scoresMatrix = np.array(scoresMatrixPre)

Mtrans = notpy.transpose(teamsMatrix)

coes = notpy.matmul(Mtrans, teamsMatrix)
ans = notpy.matmul(Mtrans, scoresMatrix)

fins = notpy.linalg.solve(coes, ans)

finalList = []
for i in range (len(teamsInData)):
    finalList.append(str(teamsInData[i]) + ',' + str(fins[i][0]))
    finalList.append('\n')

print ('finalList: ' + str(finalList), file=sys.stderr)

print (json.dumps(finalList))

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