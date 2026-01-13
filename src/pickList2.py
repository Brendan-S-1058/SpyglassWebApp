import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

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
            if comma == True:
                inputSo += char
            else:
                team += char

    finalDataDict = {}

    if inputSo == "1":
        congData = Public ()
    elif inputSo == "2":
        congData = LocalPublic (team)
    else:
        congData = Local (inputSo)

    avgData = Average(congData)
    
    #congData = '1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/'
    
    sortedList = Sort (avgData)

    for i in range (len(sortedList)):
        Break(sortedList[i], finalDataDict)

    finalList = Order (finalDataDict)

    print (json.dumps(finalList))
    
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

def Local (datain):
    start = True
    endStart = False
    dataout = ''
    for char in  datain:
        if char == ',' and start == True:
            start = False
        elif start == True and char != ',' and endStart == True:
            start = False
            dataout += char
            endStart = True
        elif start == False and char != ',':
            dataout += char
            endStart = True
        elif char == ',' and endStart == True:
            dataout += char
        if char == '/':
            start = True

    #should remove leading mode value and all leading commas

    return dataout

'''
    DataValue = ""
    dataList = []
    counta = 0
    moreData = False
    countc = 0
    leftovers = ""

    linebreak = False

    for char in datain: 
        if char != ',' and char != '/' and linebreak == False:
                DataValue = DataValue + char
        elif linebreak == True and char and char != "\n":
            moreData = True
            leftovers += char
        elif linebreak == False and char != "\"" and char != "[" and char != "]":
            counta = counta + 1
            dataList.append(DataValue)
            if counta == 1:
                nmatch = DataValue
            elif counta == 2:
                nteam = DataValue
            DataValue = ""
            if char == '/':
                linebreak = True
'''


def Average (newData):
   
    newDict = {}
    doublesDict = {}
    doublesKeys = []
    dictKeys = []
    holdS = ''
    matchStringHold = ''
    commaCount = 0
    for char in newData:
        matchStringHold += char
        if commaCount < 2:
            if char != ',':
                holdS += char
            else:
                commaCount += 1
                holdS += char
        elif char == '/':
            if holdS in dictKeys or holdS in doublesKeys:
                if holdS not in doublesKeys:

                    string1 = ''
                    list1 = []

                    for char in matchStringHold:
                        if char not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,/':
                            string1 += char
                        else:
                            if char == ',':
                                list1.append(int(string1))
                                string1 = ''

                    string2 = ''
                    list2 = []
                    for char in newDict[holdS]:
                        if char not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,/':
                            string2 += char
                        else:
                            if char == ',':
                                list2.append(int(string2))
                                string2 = ''

                    list3 = [2]
                    for i in range(len(list1)):
                        list3.append(list1[i] + list2[i])
                    
                    doublesKeys.append(holdS)
                    doublesDict[holdS] = list3

                    del newDict [holdS]
                    dictKeys.remove(holdS)

                else:
                    holdStringDoubles = ''
                    holdListDoubles = []

                    for char in matchStringHold:
                        if char not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,/':
                            holdStringDoubles += char
                        else:
                            if char == ',':
                                holdListDoubles.append(holdStringDoubles)
                                holdStringDoubles = ''
                    
                    for i in range (len(holdListDoubles)-1):
                        doublesDict[holdS][i+1] += int(holdListDoubles[i])
                    doublesDict[holdS][0] += 1

            else:
                dictKeys.append(holdS)
                newDict[holdS] = matchStringHold
            holdS = ''
            commaCount = 0
            matchStringHold = ''

    for i in doublesKeys:

        for i2 in range(len(doublesDict[i]) - 1):
            if i2 > 1:
                doublesDict[i][i2+1] /= doublesDict[i][0]
            else:
                doublesDict[i][i2+1] //= doublesDict[i][0]

        doublesDict[i].pop(0)
        
        avgString = ''
        for i2 in range(len(doublesDict[i])):
            avgString += str(doublesDict[i][i2]) + ','

        avgString += '/'

        dictKeys.append(i)
        newDict[i] = avgString
    
    finalString = ''
    for i in dictKeys:
        finalString += newDict[i]

    return (finalString)

def Sort (inputData):
    isRollover = True
    matchesByTeam = []
    while isRollover == True:
        function = 1
        startTeam = True
        teamValue = ''
        placeHTeamValue = ''
        startValue = ''
        dataLines = ''
        rollover = ''
        good = False
        bad = False
        reset = False
        for char in (inputData): 
            if function == 1:
                if char != ',':
                    startValue += char
                else:
                    function = 2
            elif function == 2:
                if char != ',':
                    if startTeam == True:
                        teamValue += char
                    placeHTeamValue += char
                else:
                    function = 3
            elif function == 3:
                if startTeam == True or teamValue == placeHTeamValue:
                    startTeam = False
                    function = 4
                    dataLines += startValue + ',' + placeHTeamValue + ',' + char
                    placeHTeamValue = ''

                else:
                    rollover += startValue + ',' + placeHTeamValue + ',' + char
                    placeHTeamValue = ''
                    function = 5
            elif function == 4:
                dataLines += char
                if char == '/':
                    function = 1
                    startValue = ''
            elif function == 5:
                rollover += char
                if char == '/':
                    function = 1
                    startValue = ''
        matchesByTeam.append (dataLines)
        if rollover == '':
            isRollover = False
        inputData = rollover         

    return matchesByTeam 

def Break (inputString, bigDict):
    hold = ''
    holdList = []
    dataLists = []
    commaCount = 0
    for char in inputString:
        if char != "," and char != "\n" and char != "\"" and char != '/':
            hold += char 
        elif char == '/':
            holdList.append(hold)
            hold = ""
            dataLists.append(holdList)
            holdList = []
            commaCount = 0
        if char == "," and commaCount != 12:
            holdList.append(hold)
            hold = ""
            commaCount += 1
    
    autoTotal = 0
    teleTotal = 0
    canBump = 'No'
    canTrench = 'No'
    holdMax = 0
    metaHoldMax = 0
    metateleTotal = 0
    shotsMade = 0
    shotsMissed = 0
    holdAClimb = 0
    holdTClimb = 0
    afuel = 0
    
    for match in dataLists:
        holdAClimb += float(match[4])
        holdTClimb += float(match[7])

        if ((float(match[9]))) > 0:
            canBump = 'Yes'
    
        if ((float(match[10]))) > 0:
            canTrench = 'Yes'
        
        shotsMade += float(match[3]) + float(match[6])
        shotsMissed += float(match[8])

        afuel += float(match[3])

        autoTotal += ((float(match[3])*1)+(float(match[4])*15))
        teleTotal += ((float(match[6])*1)+(float(match[7])*10))

        if (autoTotal + teleTotal) > holdMax or holdMax == 0:
            holdMax = float(match[3]) + float(match[4])*15 + float(match[6]) + float(match[7])*10

        if ((autoTotal + teleTotal) > metaHoldMax or metaHoldMax) and (float(match[3]) + float(match[6]) + float(match[8]) > 0):
            metaHoldMax = float(match[3]) + float(match[4])*15 + float(match[6]) + float(match[7])*10 + (10*(float(match[5])*(float(match[3]) + float(match[6]))/(float(match[3]) + float(match[6]) + float(match[8]))*(2/3)//1/10))
        #should give feed as each fed is one point times accuracy *2/3 for self feeding
        if (float(match[3]) + float(match[6]) + float(match[8]) > 0):
            metateleTotal += (float(10*(float(match[5])*(float(match[3]) + float(match[6]))/(float(match[3]) + float(match[6]) + float(match[8]))*(2/3)//1/10)))
   
    if (shotsMade + shotsMissed) > 0:
        accuracy = shotsMade/(shotsMade + shotsMissed)
    else:
        accuracy = 0
    autoAverage = autoTotal/len(dataLists)
    teleAverage = teleTotal/len(dataLists)
    metateleAverage = metateleTotal/len(dataLists)
    averageautoclimb = holdAClimb/len(dataLists)
    averageteleclimb = holdTClimb/len(dataLists)
    avgautoFuel = afuel/len(dataLists)

    metaAveragePointsScored = autoAverage + teleAverage + metateleAverage
    averagePointsScored = autoAverage + teleAverage

    bigDict[str(dataLists[0][1])] = [10*metaAveragePointsScored//1/10, 10*averagePointsScored//1/10, 10*metaHoldMax//1/10, 10*holdMax//1/10, 10*autoAverage//1/10, 10*teleAverage//1/10, 1000*accuracy//1/10, 10*averageautoclimb//1/10, 10*averageteleclimb//1/10, 10*avgautoFuel//1/10, canBump, canTrench]

def Order (inputDict):
    outerHoldList = []
    values2 = []
    outputList = []
    for i in inputDict:
        #this gives keys as i
        newHoldList = [i]
        for i2 in  (inputDict[i]):
            newHoldList.append(i2)
        outerHoldList.append(newHoldList)
    for i in outerHoldList:
        values2.append(i[1])
    values2.sort (reverse=True)
    
    while len(outerHoldList) > 0:
        cycleLength = len(outerHoldList)
        pops = 0
        for i in range (len(outerHoldList)):
            if i < cycleLength - pops:
                if outerHoldList[i][1] == values2[0]:
                    outputList.append(outerHoldList[i])
                    outerHoldList.pop(i)
                    values2.pop(0)
                    pops += 1
    
    for i in range (len(outputList)):
        outputList[i][0] = str(int(float(outputList[i][0])//1))
        for i2 in range(3):
            outputList[i][i2+1] = str(int(float(((outputList[i][i2+1])*100)//1))/100)

    for i in range (len(outputList)):
        outputList.append(outputList[0])
        outputList.append('\n')
        outputList.pop(0)
    
    finalOutputList = []
    for i in range (len(outputList)):
        holdString = ''
        for i2 in range (len(outputList[i])):
            if i2 + 1 != len(outputList[i]):
                holdString += str(outputList[i][i2]) + ','
            else:
                holdString += str(outputList[i][i2])
        finalOutputList.append(holdString)

    return (finalOutputList)

Main ()