import sys
import json

inputR = sys.stdin.read()
inputS = str(json.loads(inputR)) + ','

def Main():
    with open ("public/data/Public.txt", 'r') as file:
        currentData = file.read()
    processedInputData = makeStringList(inputS)
    with open ("public/data/Public.txt", 'w') as f:
        f.write(currentData)
        f.write(processedInputData)
        f.close ()

def processString (String):
    commaCount = 0

    for char in String:
        if char != ',':
            export_import_data += char
            one = False
        elif (one == False):
            export_import_data += char
            one = True
    return export_import_data
    
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
Main()