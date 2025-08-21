import sys
import json

inputR = sys.stdin.read()
inputS = str(json.loads(inputR)) + ','

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
        if comma == False:
            team += char
        else:
            inputSo += char



def Main(inputM, teamNum):

    #TODO: make it check for doubles

    with open ("public/data/Public.txt", 'r') as file:
        currentData = file.read()
        file.close ()
    
    with open ("public/data/Teams/" + teamNum + "/" + teamNum + "Public.txt", 'r') as file:
        teamCurrent = file.read ()
        file.close ()
    #processedInputData = makeStringList(inputS)


    compareSets = []
    matchStringHold = ''
    for char in currentData:
        matchStringHold += char
        if char == '/':
            compareSets.append(matchStringHold)
            matchStringHold = ''
    
    TeamCSets = []
    matchStringHold = ''
    for char in teamCurrent:
        matchStringHold += char
        if char == '/':
            TeamCSets.append(matchStringHold)
            matchStringHold = ''
    


    '''compareSets = []
    holdS = ''
    commaCount = 0
    for char in currentData:
        if commaCount < 2:
            if char != ',':
                holdS += char
            else:
                commaCount += 1
                holdS += char
        elif char == '/':
            compareSets.append(holdS)
            holdS = ''
            commaCount = 0 
            
            NoTE - These commented out bits are for removing duplicates of the match based on match# and team# - NOT APPLICABLE HERE - COULD BE USED with API import to check validity - or for individual team data storage 
            SHOULD BE USED IN PICKLIST FOR FINDING AVERAGES OF MATCHES SUBMITTED MULTIPLE TIMES
            '''

    newData = Local (inputM)

    secondSetForComparision = []
    matchStringHold = ''
    for char in newData:
        matchStringHold += char
        if char == '/':
            secondSetForComparision.append(matchStringHold)
            matchStringHold = ''

    for i in secondSetForComparision:
        if i not in compareSets:
            currentData += str(i)
        if i not in TeamCSets:
            teamCurrent += str(i)


    '''newDict = {}
    dictKeys = []
    holdS = ''
    matchStringHold = ''
    commaCount = 0
    for char in currentData:
        matchStringHold += char
        if commaCount < 2:
            if char != ',':
                holdS += char
            else:
                commaCount += 1
                holdS += char
        elif char == '/':
            dictKeys.append(holdS)
            holdS = ''
            commaCount = 0
            newDict[holdS] = matchStringHold

    for i in dictKeys:
        if '''
    
    print ("TRUE OUTPUT: " + currentData, file=sys.stderr)

    with open ("public/data/Public.txt", 'w') as f:
        f.write(currentData)
        f.close ()
    
    with open ("public/data/Teams/" + teamNum + "/" + teamNum + "Public.txt", 'w') as f:
        f.write(teamCurrent)
        f.close ()

def Local (datain):
    start = True
    endStart = False
    dataout = ''
    for char in  datain:
        if char == ',' and start == True:
            start = False
        elif start == True and char != ',':
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
            endStart = False
    
    #should remove leading mode value and all leading commas

    return dataout

Main(inputSo, team)
print (json.dumps("consider that public written"))