import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

    finalDataDict = {}

    if inputI == "1":
        congData = Public ()
    else:
        congData = Local (inputI)
    
    #congData = '1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/'
    
    sortedList = Sort (congData)

    for i in range (len(sortedList)):
        Break(sortedList[i], finalDataDict)

    finalList = Order (finalDataDict)

    print (json.dumps(finalList))
    
def Public ():
    with open("public/data/Public.txt","r") as f:
        rawData = f.read()
        f.close()
    
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
        if char == "," and commaCount != 28:
            holdList.append(hold)
            hold = ""
            commaCount += 1
    
    autoTotal = 0
    teleTotal = 0
    for match in dataLists:
        autoTotal += ((int(match[2])*3)+(int(match[3])*3)+(int(match[4])*4)+(int(match[5])*6)+(int(match[6])*7)+(int(match[7])*6)+(int(match[8])*4))
        teleTotal += ((int(match[9])*2)+(int(match[10])*3)+(int(match[11])*4)+(int(match[12])*5)+(int(match[13])*6)+(int(match[14])*4)+(int(match[15])*2)+(int(match[16])*6)+(int(match[17])*12))
    autoAverage = autoTotal/len(dataLists)
    teleAverage = teleTotal/len(dataLists)
    totalPointsScored = autoTotal + teleTotal
    averagePointsScored = autoAverage + teleAverage

    bigDict[str(dataLists[0][1])] = [averagePointsScored, autoAverage, teleAverage]

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
                    outputList.append('\n')
                    outerHoldList.pop(i)
                    values2.pop(0)
                    pops += 1
                    
    return (outputList)
        



    

'''
1: figure out input - public input: 1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/,100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/, or  inputR: "-1,1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/,100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/"
(
inputData: 1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/
inputData: 11058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/
)

2: figure out intended output - (start at avg points scored per team)
3: make a structure to convert input to output in both cases
4: make it sortable by multiple modes
'''

Main ()