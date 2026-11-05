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
    order = getOrder(team)

    print('order: ' + str(order), file=sys.stderr)
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


    links = []

    for i in range(len(initialOrder)):
        teamNum = initialOrder[i]
        if len(Results[teamNum]) > 0:
            Results[teamNum] = sum(Results[teamNum])/len(Results[teamNum]) + len(Results[teamNum])-i
        else:
            Results[teamNum] = len(Results[teamNum])-i

        links.append([Results[teamNum], teamNum])

    finalOrder = sorted(links, key=lambda link: link[0])

    print ('finalOrder: ' + str(finalOrder), file=sys.stderr)

    print (json.dumps(finalOrder))

    #print (Links)

    #print(finalOrder)

def getOrder(team):

    with open ("public/data/Teams/" + team + "/" + team + "baselineOrder.txt", 'r') as file:
        rawOrder = file.read()
        file.close ()

    #TODO: cry
    print ('rawOrder: ' + rawOrder, file=sys.stderr)

    return rawOrder


Main ()