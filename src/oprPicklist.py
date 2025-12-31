import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

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

    aAlliancesByMatch = {}
    tAlliancesByMatch = {}
    for match in matchsInData:
        count = 0
        aAlliancesByMatch[str(match) + 'team' + 'b'] = []
        aAlliancesByMatch[str(match) + 'team' + 'r'] = []
        aAlliancesByMatch[str(match) + 'score' + 'b'] = 0
        aAlliancesByMatch[str(match) + 'score' + 'r'] = 0
        tAlliancesByMatch[str(match) + 'team' + 'b'] = []
        tAlliancesByMatch[str(match) + 'team' + 'r'] = []
        tAlliancesByMatch[str(match) + 'score' + 'b'] = 0
        tAlliancesByMatch[str(match) + 'score' + 'r'] = 0
        for smatch in sortedData:
            if match == smatch[0]:
                #TODO: ADD REAL ALLIANCE SEPARATIONS WITH NEW INPUT PAGE
                trueoa = ((smatch[2])*3)+((smatch[3])*3)+((smatch[4])*4)+((smatch[5])*6)+((smatch[6])*7)+((smatch[7])*6)+((smatch[8])*4)
                trueot = ((smatch[9])*2)+((smatch[10])*3)+((smatch[11])*4)+((smatch[12])*5)+((smatch[13])*6)+((smatch[14])*4)+((smatch[15])*2)+((smatch[16])*6)+((smatch[17])*12)
                if count < 3:
                    aAlliancesByMatch[str(match) + 'team' + 'b'].append(smatch[1])
                    aAlliancesByMatch[str(match) + 'score' + 'b'] += trueoa
                elif count < 6:
                    aAlliancesByMatch[str(match) + 'team' + 'r'].append(smatch[1])
                    aAlliancesByMatch[str(match) + 'score' + 'r'] += trueoa
                if count < 3:
                    tAlliancesByMatch[str(match) + 'team' + 'b'].append(smatch[1])
                    tAlliancesByMatch[str(match) + 'score' + 'b'] += trueot
                elif count < 6:
                    tAlliancesByMatch[str(match) + 'team' + 'r'].append(smatch[1])
                    tAlliancesByMatch[str(match) + 'score' + 'r'] += trueot
                count += 1

    autoscores = calcCopr(teamsInData, matchsInData, aAlliancesByMatch)
    telescores = calcCopr(teamsInData, matchsInData, tAlliancesByMatch)

    Order(autoscores, telescores, state)

    print ('alliancesByMatch: ' + str(tAlliancesByMatch), file=sys.stderr)

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
        sortingDict[fins[0][i][0]+int(teamsInData[i])/100000] = teamsInData[i]
        keyList.append(fins[0][i][0]+int(teamsInData[i]/100000))

    keyList.sort(reverse=True)

    finalList = []
    for i in range (len(keyList)):
        finalList.append([(sortingDict[keyList[i]]), str(keyList[i]-int(teamsInData[i]/100000))])

    print ('finalList: ' + str(finalList), file=sys.stderr)
    return finalList

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


def Order (autolists, telelists, teamDir):

    labels = []
    xs = []
    ys = []

    for i in autolists:
        for i2 in telelists:
            if i[1] == i2[1]:
                labels.append([i[0], i2[0], i[1]])
                xs.append(i[0])
                ys.append(i2[0])


    plt.plot(xs, ys, marker='o', linestyle='None')
    plt.xlabel('Auto Average Points')
    plt.ylabel('Tele Average Points')
    for i in labels:
        plt.text(i[0], i[1], i[2])
    plt.title('Auto V. Tele')
    print ('teamDir: ' + str(teamDir), file=sys.stderr)
    filepath=("public/data/Teams/" + teamDir + "/" + teamDir + "Graphs/AVT.png")
    print ('filepath: ' + str(filepath), file=sys.stderr)
    plt.savefig(filepath, dpi=300)
    plt.close()

main ()