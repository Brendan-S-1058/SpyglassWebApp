import requests
import json
import sys

def Main():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    comma = False
    inputSo = ''
    team = ''
    for char in inputS:
        if char == ',':
            if comma == False:
                comma = True
            else:
                inputSo += char
        else:
            if comma == True:
                inputSo += char
            else:
                team += char

    #team = '2'
    #order = '2910,6324,1058,238,1678,3467,'

    with open ("public/data/Teams/" + team + "/" + team + "comps.txt", 'r') as file:
        allCompsString = file.read()
        file.close ()

    initialOrder = []
    teamNum = ''
    for char in order:
        if char == ',':
            initialOrder.append(int(teamNum))
            teamNum = ''
        else:
            teamNum += char

    allComps = []
    comp = []
    val = ''
    for char in allCompsString:
        if char == ',':
            comp.append(int(val))
            val = ''
        elif char == '/':
            comp.append(int(val))
            val = ''
            allComps.append(comp)
            comp = []
        else:
            val += char

    Results = {}
    for teamNum in initialOrder:
        Results[teamNum] = []

    for comp in allComps:
        firstWon = False
        if int(comp[2]) == 0:
            firstWon = True

        for i in range(len(initialOrder)):
            if initialOrder[i] == comp[0]:
                firstInd = i
            if initialOrder[i] == comp[1]:
                secondInd = i

        isUpset = (firstWon ^ (firstInd < secondInd))

        if isUpset:
            margin = abs(firstInd - secondInd)+1
        else:
            margin = 1/(abs(firstInd - secondInd))

        if firstWon:
            Results[comp[0]].append(margin)
            Results[comp[1]].append(-margin)
        else:
            Results[comp[0]].append(-margin)
            Results[comp[1]].append(margin)


    Links = {}

    for i in range(len(initialOrder)):
        teamNum = initialOrder[i]
        if len(Results[teamNum]) > 0:
            Results[teamNum] = sum(Results[teamNum])/len(Results[teamNum]) + len(Results[teamNum])-i + teamNum/10000000
        else:
            Results[teamNum] = len(Results[teamNum])-i

        Links[Results[teamNum]] = teamNum

    links = sorted(Links.keys(), reverse=True)

    finalOrder = []
    for key in links:
        finalOrder.append(Links[key])

    #print (Links)

    #print(finalOrder)

Main ()