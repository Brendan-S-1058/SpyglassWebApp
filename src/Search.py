import sys
import json

arrayR = []
allData = []

print ("SEARCH 1" , file=sys.stderr)

def Main ():
    global Vault
    global TeamList
    export_import_data = ""
    inputS = ""
    countd = 0
    DOUBLE = True
    #input = "1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/2,1058,1,2,1,0,4,1,1,4,4,7,4,0,1,0,0,1,No comment/"
    #inputR = sys.stdin.read()
    #inputL = json.loads(inputR)
    #for i in range (len(inputL)):
    #    inputS += inputL[i]
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))

    comma = False
    commaCount1 = 0
    inputSo = ''
    team = ''
    for char in inputS:
        if char == ',':
            commaCount1 += 1
            if comma == False:
                comma = True
            else:
                inputSo += char
        else:
            if comma == False:
                team += char
            else:
                inputSo += char

    rawData = ''

    print ('inputS: ' + str(inputS), file=sys.stderr)
    print ('len(inputS): ' + str(len(inputS)), file=sys.stderr)

    if commaCount1 < 5:
        if commaCount1 < 1:
            with open("public/data/Public.txt","r") as f:
                rawData = f.read()
                f.close()
            inputSo = team
        else:
            with open("public/data/Teams/" + team + "/" + team + 'Public.txt', 'r') as f:
                rawData = f.read()
                f.close()

        print ('len(rawData): ' + str(len(rawData)), file=sys.stderr)

        newDict = {}
        dictKeys = []
        holdS = ''
        matchStringHold = ''
        commaCount = 0
        for char in rawData:
            if char == ',':
                commaCount += 1
            matchStringHold += char
            if commaCount < 2:
                holdS += char
            elif char == '/':
                dictKeys.append(holdS)
                commaCount = 0
                newDict[holdS] = matchStringHold
                holdS = ''
                matchStringHold = ''
        
        print ('newDict: ' + str(newDict), file=sys.stderr)
        print ('dictKeys: ' + str(dictKeys), file=sys.stderr)

        congData = ''
        for i in dictKeys:
            if inputSo in i:
                congData += newDict[i]
        

        print ('congData: ' + str(congData), file = sys.stderr)
        

    else:
        congData = inputSo

    for char in congData:
        if char != "," and DOUBLE == True:
            DOUBLE = False
        if countd == 1:
            export_import_data = export_import_data + "\n"
            if char == ",":
                DOUBLE = True
        countd = 0
        if char == "/":
            countd = 1
        if DOUBLE == False:
            export_import_data = export_import_data + char
    #print("export_import_data: " + str(export_import_data), file=sys.stderr)
    NewSheet(export_import_data)

def NewSheet (datain):

    DataValue = ""
    dataList = []
    counta = 0
    moreData = False
    countc = 0
    leftovers = ""
 #   print (counta)


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

    if len(dataList)>0:
        dpresent = True
    else:
        dpresent = False

    if dpresent == True:
        
        print("dataList: " + str(dataList), file=sys.stderr)

        #auto point total
        dataList.append((int(dataList[3])*1)+(int(dataList[4])*15))
        #tele point total
        dataList.append((int(dataList[6])*1)+(int(dataList[7])*10))
        #total points scored that match
        dataList.append(dataList[13]+dataList[14])
        #score stations:
        #fuel total
        dataList.append(int(dataList[6])*1+int(dataList[3])*1)
        #climb total
        dataList.append(int(dataList[4])*15+int(dataList[7])*10)
        #fuel%
        if dataList [15]>0:
            dataList.append(round(int(dataList[16])/int(dataList[15])*100))
            #algae%
            dataList.append(round(int(dataList[17])/int(dataList[15])*100))
        else:
            dataList.append(0)
            dataList.append(0)
        #accuracy
        if (dataList[16]+int(dataList[8]) > 0):
            dataList.append(round(dataList[16]/(dataList[16]+int(dataList[8]))))
        else:
            dataList.append(0)

    allData.append(dataList)

    if moreData == True:
        NewSheet(leftovers)
    else:
        for i in range (len(allData)):
            matchS = ""
            matchL = allData[i]
            for ix in range (len(matchL)):
                matchS += str(matchL[ix])
                if ix != len(matchL) - 1:
                    matchS += ","
            arrayR.append(matchS)
            print ("array: " + str(arrayR), file=sys.stderr)


Main()
print (json.dumps(arrayR))