import sys
import json
import numpy as np

#this is going to be great
#MTMx = MTs


def main(): 
    #inputR = json.loads
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

    inputSotwo = ''
    inputSoso = ''
    section = 0
    for char in inputI:
        if char == '₯':
            section = 1
            print ('FLIPPED', file=sys.stderr)
        elif section == 0:
            inputSoso += char
        elif section == 1:
            inputSotwo += char
    

    print ('inputSoso: ' + str(inputSoso), file=sys.stderr)
    print ('inputSotwo: ' + str(inputSotwo), file=sys.stderr)
    inputI = inputSoso
    OprsByTeam = oprsort(inputSotwo)

    comma = False
    inputSo = ''
    team = ''
    for char in inputI:
        if char == ',':
            if comma == False:
                comma = True
            else:
                inputSo += char
        else:
            if comma == False:
                team += char
            else:
                inputSo += char

    print ('team: ' + team, file=sys.stderr)

    finalDataDict = {}

    if inputSo == "1":
        inputS = Public ()
    elif inputSo == "2":
        inputS = LocalPublic (team)
    else:
        '''inputS = ''
        hold = ''
        commed = False
        for char in inputSo:
            if commed == True:
                inputS += char
            elif char == ',':
                commed = True
            else:
                hold += char
        if hold != '-1':
            inputS = hold + ',' + inputS'''
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

    if (len(holdestList[0]) > len(holdestList[1])):
        holdestList[0].pop(0)

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
                totalScore = OprsByTeam[str(smatch[1])]
                totalScore -= smatch[3]+smatch[4]*15+smatch[6]+smatch[7]*10+(float(10*(float(smatch[5])*(float(smatch[3]) + float(smatch[6]))/(float(smatch[3]) + float(smatch[6]) + float(smatch[8]))*(2/3)//1/10)))
                if smatch[2] == 1:
                    alliancesByMatch[str(match) + 'team' + 'b'].append(smatch[1])
                    alliancesByMatch[str(match) + 'score' + 'b'] += totalScore
                elif smatch[2] == 0:
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

def oprsort (string):
    finalDict = {}
    holdTeam = ''
    holdScore = ''
    state = 1
    for char in string:
        if char == '/':
            finalDict[holdTeam] = int(float(holdScore))
            holdTeam = ''
            holdScore = ''
            state *= -1
        elif char == ',':
            state *= -1
        elif state == -1:
            holdScore += char
        elif state == 1:
            holdTeam += char
    finalDict[holdTeam] = int(float(holdScore))
    print ('finalDict: ' + str(finalDict), file=sys.stderr)
    return finalDict

main()