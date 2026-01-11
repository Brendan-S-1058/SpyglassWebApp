import sys
import json

print ("SEARCH 2" , file=sys.stderr)

dataLists = []
finArray = ""

def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))
    #inputS = 'matchnum, teamnum, alliance, afuel, aclimb, feed, telefuel, teleclimb, shotsmissed, canbumb, cantrench, defense, comments,,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool,23,96,119,64,40,15,54,34,13'
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
        if char == "," and commaCount != 21:
            #commacount here should be the number of items in your list because there's a trailing comma after every line
            holdList.append(hold)
            hold = ""
            commaCount += 1
        if commaCount == 21:
            #commacount here should be the number of items in your list because there's a trailing comma after every line
            dataLists.append(holdList)
            holdList = []
            commaCount = 0

    holdMax = 0
    holdMedL = []
    holdMedI = 0
    holdTotal = 0
    holdAClimb = 0
    holdTClimb = 0
    holdTAClimb = 0
    holdClimb = 0
    holdAfuel = 0
    holdFuel = 0
    holdClimbScore = 0
    holdAuto = 0
    holdAcc = 0
    holdTele = 0
    for i in range (len(dataLists)):
        holdMedL.append(int(dataLists[i][15]))
        if (int(dataLists[i][15]) > holdMax):
            holdMax = int(dataLists[i][15])
        if dataLists[i][7] == '1' or dataLists[i][7] == '2' or dataLists[i][7] == '3':
            holdTClimb += 1
        holdTotal += int(dataLists[i][15])
        holdFuel += int(dataLists[i][16])
        holdAfuel += int(dataLists[i][3])
        holdAuto += int(dataLists[i][13])
        holdAcc += float(dataLists[i][20])
        holdTele += int(dataLists[i][14])
        holdAClimb += int(dataLists[i][4])
        holdTAClimb += int(dataLists[i][7])
        holdClimb += int(dataLists[i][17])
    holdMedL.sort()
    while len(holdMedL)>2:
        holdMedL.pop(0)
        holdMedL.pop()
    if len(holdMedL)==2:
        holdMedI = (holdMedL[0]+holdMedL[1])/2
    else:
        holdMedI = holdMedL[0]
    

    print ('holdMax: ' + str(holdMax), file=sys.stderr)
    print ('holdMedL: ' + str(holdMedL), file=sys.stderr)
    print ('holdMedI: ' + str(holdMedI), file=sys.stderr)
    print ('holdTotal: ' + str(holdTotal), file=sys.stderr)
    print ('holdAClimb: ' + str(holdAClimb), file=sys.stderr)
    print ('holdTClimb: ' + str(holdTClimb), file=sys.stderr)
    print ('holdClimb: ' + str(holdClimb), file=sys.stderr)
    print ('holdAfuel: ' + str(holdAfuel), file=sys.stderr)
    print ('holdFuel: ' + str(holdFuel), file=sys.stderr)
    print ('holdAuto: ' + str(holdAuto), file=sys.stderr)
    print ('holdAcc: ' + str(holdAcc), file=sys.stderr)
    print ('holdTele: ' + str(holdTele), file=sys.stderr)


    ##Maxscore, Medianscore, Averagescore, Accuracy, AutoClimbconsistency, teleClimbconsistency, teleclimbheight, autoavg, Afuel, teleavg, fuelper, climbper, autoTavg, teleTavg
    ##//Max score, median score, average score, accuracy, auto climb consistency, tele climb consisteny, tele climb height, avg auto score, avg auto fuel, tele avg score, avg fuel percent score, avg climb percent score, avg auto percent score, avg tele percent score
    finArray+=(str(holdMax)) + ','
    finArray+=(str(holdMedI)) + ','
    finArray+=(str(holdTotal/len(dataLists))) + ','
    finArray+=(str((10*holdAcc/len(dataLists))//1/10)) + ','
    finArray+=(str((holdAClimb/len(dataLists))*100)) + ','
    finArray+=(str((holdTClimb/len(dataLists))*100)) + ','
    finArray+=(str((holdTAClimb/len(dataLists)))) + ','
    finArray+=(str((holdAfuel/len(dataLists)))) + ','
    finArray+=(str((holdAuto/len(dataLists)))) + ','
    finArray+=(str((holdTele/len(dataLists)))) + ','
    finArray+=(str((1000*holdFuel/holdTotal)//1/10)) + ','
    finArray+=(str((1000*holdClimb/holdTotal)//1/10)) + ','
    finArray+=(str(((1000*holdAuto/holdTotal))//1/10)) + ','
    finArray+=(str(((1000*holdTele/holdTotal))//1/10)) + ','
    finArray+=(str(holdClimb/len(dataLists))) + ','
    finArray+=(str(holdClimb/len(dataLists))) + ','


    print ('str(holdMax): ' + str(holdMax), file=sys.stderr)
    print ('str(holdMedI): ' + str(holdMedI), file=sys.stderr)
    print ('str(holdTotal/len(dataLists): ' + str(holdTotal/len(dataLists)), file=sys.stderr)
    print ('str(holdAcc/len(dataLists)): ' + str(holdAcc/len(dataLists)), file=sys.stderr)
    print ('holdAClimb/len(dataLists): ' + str(holdAClimb/len(dataLists)), file=sys.stderr)
    print ('holdTClimb/len(dataLists): ' + str(holdTClimb/len(dataLists)), file=sys.stderr)
    print ('holdAuto/len(dataLists): ' + str(holdAuto/len(dataLists)), file=sys.stderr)
    print ('holdAfuel/len(dataLists): ' + str(holdAfuel/len(dataLists)), file=sys.stderr)
    print ('holdTele/len(dataLists): ' + str(holdTele/len(dataLists)), file=sys.stderr)
    print ('(1000*holdFuel/holdTotal)//10: ' + str((1000*holdFuel/holdTotal)//10), file=sys.stderr)
    print ('(1000*holdClimb/holdTotal)//10: ' + str((1000*holdClimb/holdTotal)//10), file=sys.stderr)
    print ('((1000*holdAuto/holdTotal))//10: ' + str(((1000*holdAuto/holdTotal))//10), file=sys.stderr)
    print ('((1000*holdTele/holdTotal))//10: ' + str(((1000*holdTele/holdTotal))//10), file=sys.stderr)
Main ()
print (json.dumps(finArray))