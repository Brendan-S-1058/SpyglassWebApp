import pandas as pd
import os
import google.auth
import matplotlib.pyplot as plt
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import statbotics
import sys
import json

def update ():
    global Vault
    global TeamList
    global countb
    global HACK
    #input_data = "[\"6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,777/\"]\n[,,,,,,,,,,,,,,,,,,]"
    input_data = sys.stdin.read()
    with open('public/ScoutIn.txt', 'r') as file:
        holdInput = file.read ()
    with open('public/ScoutIn.txt', 'w') as f:
        f.write(holdInput)
        f.write('\n')
        f.write(input_data)
        f.close ()
    state = False
    NewSheet (state)

def Main ():

    result = {"message": f"Main"}
    print(json.dumps(result))## Could this placement be a problem?

    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = 'C:/Users/enpas/BenImpersonationProjects/Spyglass/reefscape-1058-scoutsheet-c50d49ce1b90.json'

    # Spreadsheet ID and range to update
    SPREADSHEET_ID = '1d8qs861mw2UMLWdYiq7hEsPWqjKB9y8Hv8IcM-GhqmE'  # Replace with your sheet's ID
    RANGE_NAME = 'Reefscape 2025 base - Sheet1!A1'  # Replace with your desired sheet and range

    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    # Build the service
    service = build('sheets', 'v4', credentials=credentials)

    # Read the CSV file
    df = pd.read_csv('public/Reefscape 2025 base - Sheet1.csv')  # Replace with your CSV file path

    # Replace NaN values with empty strings or a placeholder like 'N/A'
    df = df.fillna('')  # Replace NaN with an empty string

    # Convert the dataframe to a list of lists (rows)
    values = df.values.tolist()

    # Prepare the request body
    body = {
        'values': values
    }

    # Update the sheet with the CSV data
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()

    #print(f"{result.get('updatedCells')} cells updated.")

    #print ("it's main :)")
    action = "g"
    #action = input ("What do? ")
    if action == "sheet" or action == "new sheet" or action == "add data" or action == "data" or action == "match" or action == "a" or action == "add":
        NewSheet (False)
    if action == "search" or action == "find" or action == "team" or action == "team data" or action == "access vault" or action == "access Vault" or action == "f" or action == "find":
        teamFind = int(input ("What team would you like to access? "))
        teamInstanceFind = 0
        for i in range (len(TeamList)):
            if str(teamFind) == str(TeamList[i]):
                teamInstanceFind = teamInstanceFind + 1
        action2 = input ("what data would you like to see? ")
        if action2 == "auto average" or action2 == "aa":
            autoResp = 0
            for i1 in range (teamInstanceFind):
                autoResp = autoResp+int((Vault[str(teamFind)+"a"+str(i1)+"a"+str(19)]))
            #print (autoResp/teamInstanceFind)
        #elif action2 == "all" or action2 == "a":
         #   autoResp = 0
          #  for i1 in range (teamInstanceFind):
           #     for i2 in range (27):
                    ##Can continue here
            #print (autoResp/teamInstanceFind)
    if action == "main" or action == "Main" or action == "m" or action == "reset":
        Main ()
    if action == "graph" or action == "g" or action == "art" or action == "visual":
        Graph ()
    if action == "end" or action == "exit":
        exit ()

Vault = {}
countb = 0
TeamList = []

def Graph ():
   # print ("graphing")
    # Sample data
    global TeamList
    global PureTeamList
    PureTeamList = []
    TeamInstanceBool = {}
    TeamInstanceCount = {}

    teamInstanceFind = 0
    #print (TeamList)

    for i1 in range (len(TeamList)):
        TeamInstanceCount[str(TeamList[i1])] = 1
     #   print ("for 1")

    for i1 in range (len(TeamList)):
      #  print ("for 2")

        teamInstanceFind = 0
        teamInstance = 0
        for i2 in range (len(PureTeamList)):
       #     print ("for 3; pure team list")
            if str(PureTeamList[i2]) == str(TeamList[i1]):
                teamInstanceFind = teamInstanceFind + 1
            if i2 == len(PureTeamList)-1:
                TeamInstanceBool[str(TeamList[i1])] = teamInstanceFind

        TeamInstanceCount[str(TeamList[i1])] = TeamInstanceCount[str(TeamList[i1])] + teamInstanceFind

        #print (TeamInstanceCount)

        if teamInstanceFind == 0:
            PureTeamList.append (TeamList[i1])



    for i in range (len(PureTeamList)):
        xAxis = []
        yAxis = []
        for i2 in range (TeamInstanceCount[str(PureTeamList[i])]):
            xAxis.append(Vault[PureTeamList[i]+"a"+str(i2)+"a"+str(19)])
            yAxis.append(Vault[PureTeamList[i]+"a"+str(i2)+"a"+str(20)])
        
        xstorage = 0
        ystorage = 0

        for i3 in range (len(xAxis)):
            xstorage = int(xAxis[i3]) + int(xstorage)

        for i4 in range (len(yAxis)):
            ystorage = int(yAxis[i4]) + int(ystorage)

        x = xstorage/len(xAxis)
        y = ystorage/len(yAxis)

    #    print (x)
     #   print (y)

        # Specify the folder path
        folder_path = "public/ScouterGraphs"

        #Ensure the folder exists
        os.makedirs(folder_path, exist_ok=True)

        # Clear the folder of all files
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):  # Check if it's a file
                os.remove(file_path)

        # Create a plot
        plt.plot(x, y, marker='o')
        plt.title("Auto vs Tele Average Over Entire Event")
        plt.xlabel("Auto Average")
        plt.ylabel("Tele Average")
        plt.text(x, y, PureTeamList[i])

        # Save the graph in the cleared folder
        graph_file = os.path.join(folder_path, "AutoVTele.png")
        plt.savefig(graph_file)

#        print(f"Graph saved to: {graph_file}")
 #       print ("finishing graph")
  #  print ("Done graphing")

def NewSheet (passval):
    with open('public/ScoutIn.txt', 'r') as file:
        datain = file.read()
    global TeamList
    global Vault
    global countb
    exit = False
    i = 0
    DataValue = ""
    DataList = []
    counta = 0
    countc = 0
 #   print (counta)
  #  print (countb)
   # print (countc)

    linebreak = False

    for char in datain: 
        if char != ',' and char != '/' and linebreak == False:
            if countc == countb:
                DataValue = DataValue + char
        elif linebreak == False and char != "\"" and char != "[" and char != "]":
            if countc == countb:
                counta = counta + 1
                DataList.append(DataValue)
                if counta == 1:
                    nmatch = DataValue
                elif counta == 2:
                    nteam = DataValue
                DataValue = ""
            if char == '/':
                countc = countc + 1
                if countc == countb + 1:
                    countb = countb + 1
                    linebreak = True

    if len(DataList)>0:
        dpresent = True
    else:
        dpresent = False

    if dpresent == True:
        
        #auto point total
        DataList.append((int(DataList[2])*3)+(int(DataList[3])*3)+(int(DataList[4])*4)+(int(DataList[5])*6)+(int(DataList[6])*7)+(int(DataList[7])*6)+(int(DataList[8])*4))
        #tele point total
        DataList.append((int(DataList[9])*2)+(int(DataList[10])*3)+(int(DataList[11])*4)+(int(DataList[12])*5)+(int(DataList[13])*6)+(int(DataList[14])*4)+(int(DataList[15])*2)+(int(DataList[16])*6)+(int(DataList[17])*12))
        #total points scored that match
        DataList.append(DataList[19]+DataList[20])
        #score stations:
        #coral total
        DataList.append(int(DataList[3])*3+int(DataList[4])*4+int(DataList[5])*6+int(DataList[6])*7+int(DataList[9])*2+int(DataList[10])*3+int(DataList[11])*4+int(DataList[12])*5)
        #algae total
        DataList.append(int(DataList[7])*6+int(DataList[8])*4+int(DataList[13])*6+int(DataList[14])*4)
        #location total 
        DataList.append(int(DataList[2])*3+int(DataList[15])*2+int(DataList[16])*6+int(DataList[17])*12)
        #coral%
        DataList.append(round(int(DataList[22])/int(DataList[21])*100))
        #algae%
        DataList.append(round(int(DataList[23])/int(DataList[21])*100))
        #location%
        DataList.append(round(int(DataList[24])/int(DataList[21])*100))

    #add all processes here, make vault hold key information
    ###imported EPA and OPR from blue alliance --need internet
    ###???percent of team's score, needs imported alliance score from blue alliance and total. May be impractical considering Blue Alliance's delay???
    ###create separate outputs/sheets/including graphs???

        teamInstance = 0

        for i in range (len(TeamList)):
            if TeamList[i] == nteam:
                teamInstance = teamInstance + 1

        standTeam = str(nteam)+"a"+str(teamInstance)

        for i in range (28):
            if DataList[i] != "/n1" and DataList != nteam:
                if i>1:
                    Vault[standTeam+"a"+str(i)] = (DataList[i])
                else:
                    Vault[standTeam+"a"+str(i)] = True
            else:
                Vault[standTeam+"a"+str(i)] = True
        
        
        TeamList.append (nteam)       

        epa = statbotics.Statbotics()
        epaList = epa.get_team(int(nteam))
        norm_epa = (epaList['district'])
        DataList.append(norm_epa)
        DataList.append (epa)
        
        if passval == True:
            with open('public/Reefscape 2025 base - Sheet1.csv', 'r') as file:
                hold = file.read ()
        else:
            hold = "What in the heck,placeholders,in,this,line,seem,to,get,ignored,as,long,as,they,are,the,first,line,and,no,longer,than,the,list,of,values,that,will,be,added,mustbeequal\nMatch Number,Team Number,Auto Move,L1 auto,L2 auto,L3 auto,L4 auto,processor auto, net auto,L1 tele,L2 tele,L3 tele,L4 tele,processor tele,net tele,park end,shallow cage end,deep cage end,auto total,tele total,total,coral score,algae score,location score,coral score %,algae score %,location score %,average score at event,natural epa,comments\n"
        with open('public/Reefscape 2025 base - Sheet1.csv', 'w') as f:
            f.write(hold)
            f.write(str(DataList[0])+',')
            f.write(str(DataList[1])+",")
            f.write(str(DataList[2])+",")
            f.write(str(DataList[3])+",")
            f.write(str(DataList[4])+",")
            f.write(str(DataList[5])+",")
            f.write(str(DataList[6])+",")
            f.write(str(DataList[7])+",")
            f.write(str(DataList[8])+",")
            f.write(str(DataList[9])+",")
            f.write(str(DataList[10])+",")
            f.write(str(DataList[11])+",")
            f.write(str(DataList[12])+",")
            f.write(str(DataList[13])+",")
            f.write(str(DataList[14])+",")
            f.write(str(DataList[15])+",")
            f.write(str(DataList[16])+",")
            f.write(str(DataList[17])+",")
            f.write(str(DataList[19])+",")
            f.write(str(DataList[20])+",")
            f.write(str(DataList[21])+",")
            f.write(str(DataList[22])+",")
            f.write(str(DataList[23])+",")
            f.write(str(DataList[24])+",")
            f.write(str(DataList[25])+",")
            f.write(str(DataList[26])+",")
            f.write(str(DataList[27])+",")
            f.write(str(DataList[28])+",")
            runningTotal = 0
            for i in range (teamInstance+1):
                runningTotal = int(Vault[nteam+"a"+str(i)+"a"+str(21)]) + runningTotal
            f.write(str(runningTotal/(teamInstance+1))+",")
            f.write(str(DataList[18]))
            state = True
        NewSheet (state)
    elif dpresent == False:
        #print (len(Vault))
        Main ()

update ()