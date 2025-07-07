import sys
import json

def Main ():
    #inputR = sys.stdin.read()
    #inputI = json.loads(inputR)

    #print ('inputR: ' + str(inputR))

    #if inputI == "1":
        #congData = Public ()
    #else:
        #congData = Local (inputI)
    
    congData = '1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/'
    
    sortedList = Sort (congData)

    print ("sortedList: " + str(sortedList))

def Public ():
    with open("public/data/Public.txt","r") as f:
        rawData = f.read()
        f.close()
    
    #print ("public input: " + str(rawData))

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

    #print ("dataout: " + str(dataout))

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
    #print ("inputData: " + str(inputData))

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
                    dataLines += startValue + ',' + placeHTeamValue
                    placeHTeamValue = ''

                else:
                    rollover += startValue + ',' + placeHTeamValue
                    placeHTeamValue = ''
                    #print ('rollover: ' + str(rollover))
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