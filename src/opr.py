import sys
import json
import numpy as np

#this is going to be great
#MTMx = MTs


def main(): 
    #inputR = json.loads
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)
    setting = 0
    state = ''
    dataH = ''

    for char in inputI:
        if char == '@':
            setting = 1
        elif setting == 0:
            state += char
        elif setting == 1:
            dataH += char
    
    inputI = dataH
    
    print ('state: ' + state, file=sys.stderr)
            
    comma = -1
    inputSo = ''
    team = ''
    for char in inputI:
        if char == ',':
            if comma < 1:
                comma += 1
            else:
                inputSo += char
        else:
            if comma < 1:
                team += char
            else:
                inputSo += char

    print ('team: ' + team, file=sys.stderr)

    if inputSo == "1":
        inputS = Public ()
    elif inputSo == "2":
        inputS = LocalPublic (team)
    else:
        inputS = inputSo

    print ('inputS: ' + str(inputS), file=sys.stderr)

    hold = ''
    holdList = []
    for char in inputS:
        if char == '/':
            holdList.append(hold)
            hold = ''
        else:
            hold += char

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
        alliancesByMatch[str(match) + 'team' + 'b'] = []
        alliancesByMatch[str(match) + 'team' + 'r'] = []
        alliancesByMatch[str(match) + 'score' + 'b'] = 0
        alliancesByMatch[str(match) + 'score' + 'r'] = 0
        for smatch in sortedData:
            if match == smatch[0]:
                #TODO: ADD REAL ALLIANCE SEPARATIONS WITH NEW INPUT PAGE
                trueo = trueOpr(smatch, state)
                if count < 3:
                    alliancesByMatch[str(match) + 'team' + 'b'].append(smatch[1])
                    alliancesByMatch[str(match) + 'score' + 'b'] += trueo
                elif count < 6:
                    alliancesByMatch[str(match) + 'team' + 'r'].append(smatch[1])
                    alliancesByMatch[str(match) + 'score' + 'r'] += trueo
                count += 1

    calcCopr(teamsInData, matchsInData, alliancesByMatch)

    print ('alliancesByMatch: ' + str(alliancesByMatch), file=sys.stderr)

def trueOpr(smatch, state):
    if state == 'opr':
        return (((smatch[2])*3)+((smatch[3])*3)+((smatch[4])*4)+((smatch[5])*6)+((smatch[6])*7)+((smatch[7])*6)+((smatch[8])*4)+((smatch[9])*2)+((smatch[10])*3)+((smatch[11])*4)+((smatch[12])*5)+((smatch[13])*6)+((smatch[14])*4)+((smatch[15])*2)+((smatch[16])*6)+((smatch[17])*12))
    elif state == 'l1c':
        return smatch[3]+smatch[9]
    elif state == 'l2c':
        return smatch[4]+smatch[10]
    elif state == 'l3c':
        return smatch[5]+smatch[11]
    elif state == 'l4c':
        return smatch[6]+smatch[12]
    elif state == 'tcc':
        return smatch[3]+smatch[4]+smatch[5]+smatch[6]+smatch[9]+smatch[10]+smatch[11]+smatch[12]
    elif state == 'tcs':
        return smatch[3]*3+smatch[4]*4+smatch[5]*6+smatch[6]*7+smatch[9]*2+smatch[10]*3+smatch[11]*4+smatch[12]*5
    elif state == 'tac':
        return smatch[7]+smatch[8]+smatch[13]+smatch[14]
    elif state == 'tgpc':
        return smatch[3]+smatch[4]+smatch[5]+smatch[6]+smatch[9]+smatch[10]+smatch[11]+smatch[12]+smatch[7]+smatch[8]+smatch[13]+smatch[14]
    elif state == 'acc':
        return smatch[3]+smatch[4]+smatch[5]+smatch[6]
    elif state == 'ams':
        return smatch[2]
    elif state == 'taus':
        return ((smatch[2])*3)+((smatch[3])*3)+((smatch[4])*4)+((smatch[5])*6)+((smatch[6])*7)+((smatch[7])*6)+((smatch[8])*4)
    elif state == 'tecc':
        return smatch[9]+smatch[10]+smatch[11]+smatch[12]
    elif state == 'tas':
        return (smatch[7]*6+smatch[8]*4+smatch[13]*6+smatch[14]*4)
    elif state == 'tna':
        return smatch[8]+smatch[14]
    elif state == 'tpa':
        return smatch[7]+smatch[13]

def calcCopr(teamsInData, matchsInData, alliancesByMatch):
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
            scoresMatrixPre.append([alliancesByMatch[str(match)+'score'+'b']])
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
            scoresMatrixPre.append([alliancesByMatch[str(match)+'score'+'r']])

    print ('teamsMatrixPre: ' + str(teamsMatrixPre), file=sys.stderr)
    print ('scoresMatrixPre: ' + str(scoresMatrixPre), file=sys.stderr)


    teamsMatrix = np.array(teamsMatrixPre)
    scoresMatrix = np.array(scoresMatrixPre)

    Mtrans = np.transpose(teamsMatrix)

    coes = np.matmul(Mtrans, teamsMatrix)
    ans = np.matmul(Mtrans, scoresMatrix)

    fins = np.linalg.lstsq(coes, ans)

    sortingDict = {}
    keyList = []
    for i in range (len(teamsInData)):
        sortingDict[fins[0][i][0]] = teamsInData[i]
        keyList.append(fins[0][i][0])

    keyList.sort(reverse=True)

    finalList = []
    for i in range (len(keyList)):
        finalList.append(str(sortingDict[keyList[i]]) + ',' + str(keyList[i])) 
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

def Public ():
    with open("public/data/Public.txt","r") as f:
        rawData = f.read()
        f.close()
    
    return rawData

def LocalPublic (team):
    with open ("public/data/Teams/" + team + "/" + team + 'Public.txt', 'r') as file:
        rawData = file.read ()
        file.close ()
    
    return rawData

main()