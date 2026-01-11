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

    comma = False
    inputSo = ''
    team = ''
    for char in inputS:
        if char == ',':
            if comma == False:
                comma = True
            else:
                inputSo += char
        else:
            if comma == False:
                team += char
            else:
                inputSo += char

    print ('inputSo: ' + str(inputSo), file=sys.stderr)

    #team #	match #	auto move	auto L1	auto L2	auto L3	auto L4	auto Processor	auto Net	tele L1	tele L2	tele L3	tele L4	tele processor	tele net	end park	end shallow cage	end deep cage	comments	actions
    #1058	1	1	2	1	2	4	1	1	4	4	4	4	1	1	0	0	1	No comment	Delete

    #inputS = '1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool,'
    holdList = []
    hold = ""
    one = True
    export_import_data = ""
    inputSo += ','

    for char in inputSo:
        if char != ',':
            export_import_data += char
            one = False
            if char == '/':
                one = True
        elif (one == False):
            export_import_data += char
            one = True
    
    for char in export_import_data:
        if char != "," and char != "\n" and char != "/":
            hold += char 
            #print (hold)
        if char == "," or char == '/':
            holdList.append(hold)
            hold = ""
        if char == '/':
            dataLists.append(holdList)
            holdList = []
    
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
                autoTotal = ((int(match[3])*1)+(int(match[4])*15))
                teleTotal = ((int(match[6])*1)+(int(match[7])*10))
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
            filepath=('public/data/Teams/' + str(team) + '/' + str(team) + 'Graphs/' + str(currentTeam) + ".png")
            plt.savefig(filepath, dpi=300)
            plt.close()

            plt.plot(teleTotalXAxis2, autoTotalYAxis2, marker='o', linestyle='None')
            plt.xlabel('Tele Total')
            plt.ylabel('Auto Total')
            plt.title(str(currentTeam) + " Auto V. Tele")
            #filepath=os.path.join(str(currentTeam) + "avt.png")
            filepath=('public/data/Teams/' + str(team) + '/' + str(team) + 'Graphs/' + str(currentTeam) + "avt.png")
            plt.savefig(filepath, dpi=300)
            plt.close()

Main ()
print (json.dumps("NO ERRORS YAY"))