import pandas as pd
import os
import matplotlib.pyplot as plt
import statbotics
import sys
import json
import gspread

allData = []

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
    #inputR = sys.stdin.read()
    inputS = str(sys.stdin.read())
    print("inputS: " + inputS, file=sys.stderr)


    ##TODO: multiple lines are not working correctly. data passage problem?? presumably the input was not ok

    for char in inputS:
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
    print("export_import_data: " + str(export_import_data), file=sys.stderr)
    NewSheet(export_import_data)

def NewSheet (datain):

    DataValue = ""
    dataList = []
    array = []
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
        
        #auto point total
        dataList.append((int(dataList[2])*3)+(int(dataList[3])*3)+(int(dataList[4])*4)+(int(dataList[5])*6)+(int(dataList[6])*7)+(int(dataList[7])*6)+(int(dataList[8])*4))
        #tele point total
        dataList.append((int(dataList[9])*2)+(int(dataList[10])*3)+(int(dataList[11])*4)+(int(dataList[12])*5)+(int(dataList[13])*6)+(int(dataList[14])*4)+(int(dataList[15])*2)+(int(dataList[16])*6)+(int(dataList[17])*12))
        #total points scored that match
        dataList.append(dataList[19]+dataList[20])
        #score stations:
        #coral total
        dataList.append(int(dataList[3])*3+int(dataList[4])*4+int(dataList[5])*6+int(dataList[6])*7+int(dataList[9])*2+int(dataList[10])*3+int(dataList[11])*4+int(dataList[12])*5)
        #algae total
        dataList.append(int(dataList[7])*6+int(dataList[8])*4+int(dataList[13])*6+int(dataList[14])*4)
        #location total 
        dataList.append(int(dataList[2])*3+int(dataList[15])*2+int(dataList[16])*6+int(dataList[17])*12)
            #coral%
        if dataList [21]>0:
            dataList.append(round(int(dataList[22])/int(dataList[21])*100))
            #algae%
            dataList.append(round(int(dataList[23])/int(dataList[21])*100))
            #location%
            dataList.append(round(int(dataList[24])/int(dataList[21])*100))
        else:
            dataList.append(0)
            dataList.append(0)
            dataList.append(0)

    allData.append(dataList)

    if moreData == True:
        NewSheet(leftovers)
    else:
        for i in range (len(allData)):
            matchS = ""
            matchL = allData[i]
            for ix in range (len(matchL)):
                matchS += str(matchL[ix]) + ","
            array.append(matchS)
            print ("array: " + str(array), file=sys.stderr)
            print (json.dumps(array))


Main()