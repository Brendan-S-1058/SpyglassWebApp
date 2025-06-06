import sys
import json

inputR = sys.stdin.read()
inputS = str(json.loads(inputR)) + ','

def Main():
    with open ("public/data/Public.txt", 'r') as file:
        currentData = file.read()
    processedCurrentData = makeStringList(currentData)
    processedInputData = makeStringList(inputS)

def makeStringList (String):
    for char in String:
        if char != ',':
            export_import_data += char
            one = False
        elif (one == False):
            export_import_data += char
            one = True
    
    for char in export_import_data:
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

    return dataLists

    print (processedCurrentData)
    print (processedInputData)
Main()