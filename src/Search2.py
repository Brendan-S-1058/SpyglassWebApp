import sys
import json

dataLists = []
finArray = ""

def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))
    #inputS = '1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment,63,78,141,106,20,15,75,14,11,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool,23,96,119,64,40,15,54,34,13'
    holdList = []
    hold = ""
    global finArray
    commaCount = 0
    DOUBLE = True
    countd = 0
    export_import_data = ""

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

    export_import_data += ","

    for char in export_import_data:
        if char != "," and char != "\n" and char != "\"":
            hold += char 
            #print (hold)
        if char == "," and commaCount != 28:
            holdList.append(hold)
            hold = ""
            commaCount += 1
        if commaCount == 28:
            dataLists.append(holdList)
            holdList = []
            commaCount = 0
    
    holdMax = 0
    holdMedL = []
    holdMedI = 0
    holdTotal = 0
    holdAlgae = 0
    holdCoral = 0
    holdAuto = 0
    holdTele = 0
    holdLoc = 0 
    holdClimb = 0
    for i in range (len(dataLists)):
        holdMedL.append(int(dataLists[i][21]))
        if (int(dataLists[i][21]) > holdMax):
            holdMax = int(dataLists[i][21])
        if dataLists[i][16] == '1' or dataLists[i][17] == '1':
            holdClimb += 1
        holdTotal += int(dataLists[i][21])
        holdAlgae += int(dataLists[i][23])
        holdCoral += int(dataLists[i][22])
        holdAuto += int(dataLists[i][19])
        holdTele += int(dataLists[i][20])
        holdLoc += int(dataLists[i][24])
    holdMedL.sort()
    while len(holdMedL)>2:
        holdMedL.pop(0)
        holdMedL.pop()
    if len(holdMedL)==2:
        holdMedI = (holdMedL[0]+holdMedL[1])/2
    else:
        holdMedI = holdMedL[0]
    ##Maxscore, Medianscore, Averagescore, Climbconsistency, algaeavg, coralavg,locationavg, teleTavg, autoTavg, autoavg, teleavg
    ##//Max score, median score, average score,climb, avg algae score, avg coral score, avg loc score, avg auto score, avg tele score, avg auto % total score, avg tele % total score
    finArray+=(str(holdMax)) + ','
    finArray+=(str(holdMedI)) + ','
    finArray+=(str(holdTotal/len(dataLists))) + ','
    finArray+=(str((holdClimb/len(dataLists))*100)) + ','
    finArray+=(str(holdLoc/len(dataLists))) + ','
    finArray+=(str(holdAlgae/len(dataLists))) + ','
    finArray+=(str(holdCoral/len(dataLists))) + ','
    finArray+=(str(holdAuto/len(dataLists))) + ','
    finArray+=(str(holdTele/len(dataLists))) + ','
    finArray+=(str(((holdAuto/holdTotal)*1000)//10)) + ','
    finArray+=(str(((holdTele/holdTotal)*1000)//10)) + ','
Main ()
print (json.dumps(finArray))