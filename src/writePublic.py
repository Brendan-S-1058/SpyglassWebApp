import sys
import json

inputR = sys.stdin.read()
inputS = str(json.loads(inputR)) + ','

def Main():

    #TODO: make it check for doubles

    with open ("public/data/Public.txt", 'r') as file:
        currentData = file.read()
        file.close ()
    #processedInputData = makeStringList(inputS)


    compareSets = []
    matchStringHold = ''
    for char in currentData:
        matchStringHold += char
        if char == '/':
            compareSets.append(matchStringHold)
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

    newData = Local (inputS)

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

def Local (datain):
    start = True
    endStart = False
    dataout = ''
    print ("WP PRINTS: input: " + str (datain), file=sys.stderr)
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
    print ("WP PRINTS: output:" + str (dataout), file=sys.stderr)
    
    #should remove leading mode value and all leading commas

    return dataout

Main()
print (json.dumps("consider that public written"))