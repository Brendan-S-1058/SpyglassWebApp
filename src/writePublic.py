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

    allData = Local (currentData + inputS)

    with open ("public/data/Public.txt", 'w') as f:
        f.write(allData)
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

"""def processString (String):
    '''
    What Do I need to do for this:
    find key information
    sort it
    return it
    '''
    
    '''for char in export_import_data:
        if char != "," and char != "\n" and char != "\"":
            hold += char 
            #print (hold)
        if char == "," and commaCount != 28:
            holdList.append(hold)
            hold = ""
            commaCount += 1
        if commaCount == 19:
            dataLists.append(holdList)
            holdList = []
            commaCount = 0
    
    returnString = ''
    commas = 0
    FIRST = True
    
    for outerI in range (len(holdList)):
        for innerI in range (holdList[0]):
            returnString += holdList[0][innerI]
            if FIRST == False and commas < 28:
                returnString += ','
                commas += 1
            if 
            FIRST = False
      '''      

    #return dataLists
"""
Main()
print (json.dumps("consider that public written"))