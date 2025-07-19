import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

dataLists = []
teamCount = []
major = []
alreadyRun = []
def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))

    #team #	match #	auto move	auto L1	auto L2	auto L3	auto L4	auto Processor	auto Net	tele L1	tele L2	tele L3	tele L4	tele processor	tele net	end park	end shallow cage	end deep cage	comments	actions
    #1058	1	1	2	1	2	4	1	1	4	4	4	4	1	1	0	0	1	No comment	Delete

    #inputS = '1058,1,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment,,1058,100,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool,,3467,100,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool,'
    holdList = []
    hold = ""
    one = True
    commaCount = 0
    export_import_data = ""
    inputS += ','

    for char in inputS:
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
    
    for i in range (len(dataLists)):
        if dataLists[i] not in teamCount:
            teamCount.append(dataLists[i][1])

    for i in range (len(teamCount)):
        hold2list = []
        if teamCount[i] not in (alreadyRun):
            for i2 in range (len(dataLists)):
                if teamCount[i] in dataLists[i2][1]:
                    hold2list.append(dataLists[i2])
            major.append (hold2list)
        alreadyRun.append (teamCount[i])
    
    for i in range (len(teamCount)):
        if i < len(major):
            pointsTotalYAxis1 = []
            matchNumberXAxis1 = []
            autoTotalYAxis2 = []
            teleTotalXAxis2 = []
            for match in major[i]:
                currentTeam = match[1]
                autoTotal = ((int(match[2])*3)+(int(match[3])*3)+(int(match[4])*4)+(int(match[5])*6)+(int(match[6])*7)+(int(match[7])*6)+(int(match[8])*4))
                teleTotal = ((int(match[9])*2)+(int(match[10])*3)+(int(match[11])*4)+(int(match[12])*5)+(int(match[13])*6)+(int(match[14])*4)+(int(match[15])*2)+(int(match[16])*6)+(int(match[17])*12))
                autoTotalYAxis2.append(autoTotal)
                teleTotalXAxis2.append(teleTotal)                
                pointsTotalYAxis1.append(autoTotal + teleTotal)
                matchNumberXAxis1.append(match[0])

            print ('matchNumberXAxis1: ' + str(matchNumberXAxis1), file=sys.stderr)
            print ('pointsTotalYAxis1: ' + str(pointsTotalYAxis1), file=sys.stderr)

            print ('teleTotalXAxis2: ' + str(teleTotalXAxis2), file=sys.stderr)
            print ('autoTotalYAxis2: ' + str(autoTotalYAxis2), file=sys.stderr)

            plt.plot(matchNumberXAxis1, pointsTotalYAxis1, marker='o', linestyle='-', color='b')
            plt.xlabel('Match #')
            plt.ylabel('Total Points Scores')
            plt.title(str(currentTeam))
            #filepath=os.path.join(str(currentTeam) + ".png")
            filepath=("public/data/ScouterGraphs/" + str(currentTeam) + ".png")
            plt.savefig(filepath, dpi=300)
            plt.close()

            plt.plot(teleTotalXAxis2, autoTotalYAxis2, marker='o')
            plt.xlabel('Tele Total')
            plt.ylabel('Auto Total')
            plt.title(str(currentTeam) + " Auto V. Tele")
            #filepath=os.path.join(str(currentTeam) + "avt.png")
            filepath=("public/data/ScouterGraphs/" + str(currentTeam) + "avt.png")
            plt.savefig(filepath, dpi=300)
            plt.close()

Main ()
print (json.dumps("NO ERRORS YAY"))