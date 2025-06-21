import sys
import json

inputR = sys.stdin.read()
inputS = str(json.loads(inputR)) + ','

def Main():
    with open ("public/data/Public.txt", 'r') as file:
        currentData = file.read()
        file.close ()
    #processedInputData = makeStringList(inputS)
    with open ("public/data/Public.txt", 'w') as f:
        f.write(currentData)
        f.write(inputS)
        f.close ()

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