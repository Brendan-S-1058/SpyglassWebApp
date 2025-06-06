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
import gspread
from googleapiclient.http import MediaFileUpload

def update ():
    global Vault
    global TeamList
    global countb
    export_import_data = ""
    countd = 0
    DOUBLE = True
    #input_data = ""
    #input_data = "30,1690,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Nothing/,,20,1690,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Nothing/"
    input_data = sys.stdin.read()
    for char in input_data:
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
    with open('public/data/ScoutIn.txt', 'r') as file:
        holdInput = file.read ()
    with open('public/data/ScoutIn.txt', 'w') as f:
        f.write(holdInput)
        f.write('\n')
        f.write(export_import_data)
        f.close ()
    state = False
    NewSheet (state)

def Main ():

    global client
    global SPREADSHEET_ID

    result = {"message": f"Main"}
    print(json.dumps(result))## Could this placement be a problem?

    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = '/etc/secrets/GOOGLE_CREDENTIALS'

    # Spreadsheet ID and range to update
    #GSD Sheet
    #SPREADSHEET_ID = '1d8qs861mw2UMLWdYiq7hEsPWqjKB9y8Hv8IcM-GhqmE'  # Replace with your sheet's ID
    #SPREADSHEET_ID = '1js3i_A4MGj8RY3AIyMJ9Oxmc68hbqt8u8l_TjY-5IpU'
    SPREADSHEET_ID = '1qaikUbJbw4dKaAzEX8JDI16yrgazJW8jCHsNGCB9j4Q'
    RANGE_NAME = '!A1'  # Replace with your desired sheet and range

    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes = ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/spreadsheets"]       
        )

    client = gspread.authorize(credentials)

    # Build the service
    service = build('sheets', 'v4', credentials=credentials)

    # Read the CSV file
    df = pd.read_csv('public/data/Reefscape 2025 base - Sheet1.csv')  # Replace with your CSV file path

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
        valueInputOption="USER_ENTERED",
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
    global TeamInstanceCount
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
            HoldingList = []
            for i7 in range (len(PureTeamList)):
                HoldingList.append(int(PureTeamList[i7]))
            HoldingList.sort ()
            PureTeamList = []
            for i8 in range (len(HoldingList)):
                PureTeamList.append(str(HoldingList[i8]))



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
        folder_path = "public/data/ScouterGraphs"

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
    NewTab ()

#        print(f"Graph saved to: {graph_file}")
 #       print ("finishing graph")
  #  print ("Done graphing")

def NewSheet (passval):
    with open('public/data/ScoutIn.txt', 'r') as file:
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
        if DataList [21]>0:
            DataList.append(round(int(DataList[22])/int(DataList[21])*100))
            #algae%
            DataList.append(round(int(DataList[23])/int(DataList[21])*100))
            #location%
            DataList.append(round(int(DataList[24])/int(DataList[21])*100))
        else:
            DataList.append(0)
            DataList.append(0)
            DataList.append(0)

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
                    Vault[standTeam+"a"+str(i)] = nmatch
            else:
                Vault[standTeam+"a"+str(i)] = nteam
        
        
        TeamList.append (nteam)       
        
        epa = statbotics.Statbotics()
        epaList = epa.get_team(int(nteam))
        norm_epa = (epaList['norm_epa'])
        norm_epa = (norm_epa['current'])
        DataList.append(norm_epa)

        #DataList.append("UNCOMMENT EPA")
        if passval == True:
            with open('public/data/Reefscape 2025 base - Sheet1.csv', 'r') as file:
                hold = file.read ()
        else:
            hold = "What in the heck,placeholders,in,this,line,seem,to,get,ignored,as,long,as,they,are,the,first,line,and,no,longer,than,the,list,of,values,that,will,be,added,mustbeequal\nMatch Number,Team Number,Auto Move,L1 auto,L2 auto,L3 auto,L4 auto,processor auto, net auto,L1 tele,L2 tele,L3 tele,L4 tele,processor tele,net tele,park end,shallow cage end,deep cage end,auto total,tele total,total,coral score,algae score,location score,coral score %,algae score %,location score %,average score at event,natural epa,comments\n"
        with open('public/data/Reefscape 2025 base - Sheet1.csv', 'w') as f:
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
            runningTotal = 0
            for i in range (teamInstance+1):
                runningTotal = int(Vault[nteam+"a"+str(i)+"a"+str(21)]) + runningTotal
            DataList.append(runningTotal/(teamInstance+1))
            Vault[nteam+"a"+str(teamInstance)+"a"+str(29)] = DataList[29]
            Vault[nteam+"a"+str(teamInstance)] = (((str(DataList[0])+',')
            + (str(DataList[1])+",")
            + (str(DataList[2])+",")
            + (str(DataList[3])+",")
            + (str(DataList[4])+",")
            + (str(DataList[5])+",")
            + (str(DataList[6])+",")
            + (str(DataList[7])+",")
            + (str(DataList[8])+",")
            + (str(DataList[9])+",")
            + (str(DataList[10])+",")
            + (str(DataList[11])+",")
            + (str(DataList[12])+",")
            + (str(DataList[13])+",")
            + (str(DataList[14])+",")
            + (str(DataList[15])+",")
            + (str(DataList[16])+",")
            + (str(DataList[17])+",")
            + (str(DataList[19])+",")
            + (str(DataList[20])+",")
            + (str(DataList[21])+",")
            + (str(DataList[22])+",")
            + (str(DataList[23])+",")
            + (str(DataList[24])+",")
            + (str(DataList[25])+",")
            + (str(DataList[26])+",")
            + (str(DataList[27])+",")
            + (str(DataList[29])+",")
            + (str(DataList[28])+",")
            + (str(DataList[18]))))
            f.write(str(runningTotal/(teamInstance+1))+",")
            f.write(str(DataList[28])+",")
            f.write(str(DataList[18]))
            state = True
        NewSheet (state)
    elif dpresent == False:
        #print (len(Vault))
        Main ()

def NewTab ():
    global Vault
    global TeamList
    global PureTeamList
    global client
    global SPREADSHEET_ID
    global TeamInstanceCount

    ca = 0
    
    SERVICE_ACCOUNT_FILE = '/etc/secrets/GOOGLE_CREDENTIALS'
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    sheet_names = [sheet.title for sheet in spreadsheet.worksheets()]
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    for i in range (len(PureTeamList)):
        if PureTeamList[i] not in sheet_names:
            spreadsheet.add_worksheet (title=PureTeamList[i], rows="100", cols="40")
    if "Pick List" not in sheet_names:
        spreadsheet.add_worksheet (title="Pick List", rows="100", cols="40")

    #Need calling information for Vault:

    #team number: PureTeamList[i]
    #said team's number of matches: TeamInstancecount[PureTeamList[i]]
    #information location in list (1-30)
    sheet_names = [sheet.title for sheet in spreadsheet.worksheets()]
    for i2 in range (len(PureTeamList)):
        tabData = ""
        pureTabData = ""
        totalScores = []
        countf = 0
        Match = ""
        for i3 in range (TeamInstanceCount[PureTeamList[i2]]):
            tabData = tabData + str(Vault[PureTeamList[i2]+"a"+str(i3)]) + ','
            totalScores.append(int(Vault[PureTeamList[i2]+"a"+str(i3)+"a"+str(20)]))
        maxscore = max(totalScores)
        for i3 in range (TeamInstanceCount[PureTeamList[i2]]):
            if (int(Vault[PureTeamList[i2]+"a"+str(i3)+"a"+str(20)]) == maxscore):
                match = str(i3)

        for char in tabData:
            if char != ',':
                pureTabData = pureTabData + char
            else:
                countf = countf + 1
                if countf == 30:
                    countf = 0
                else:            
                    pureTabData = pureTabData + char
        with open ("public/data/TabData.csv", 'w') as file:
            file.write ("What in the heck,placeholders,in,this,line,seem,to,get,ignored,as,long,as,they,are,the,first,line,and,no,longer,than,the,list,of,values,that,will,be,added,mustbeequal\nMatch Number,Team Number,Auto Move,L1 auto,L2 auto,L3 auto,L4 auto,processor auto, net auto,L1 tele,L2 tele,L3 tele,L4 tele,processor tele,net tele,park end,shallow cage end,deep cage end,auto total,tele total,total,coral score,algae score,location score,coral score %,algae score %,location score %,average score at event,natural epa,comments\n")
            file.write (str(pureTabData)+"\n")
            file.write ("max score:,=MAX(U2:U"+str(TeamInstanceCount[PureTeamList[i2]]+1)+")")
            file.write (",max score delta processor:,=MAX(U2:U"+str(TeamInstanceCount[PureTeamList[i2]]+1)+")-4*("+(str(Vault[str(PureTeamList[i2])+"a"+str(match)+"a"+str(13)]))+"+"+str(Vault[str(PureTeamList[i2])+"a"+str(match)+"a"+str(7)])+")")

        tab = pd.read_csv('public/data/TabData.csv')
        tab = tab.fillna('')
        values = tab.values.tolist()

        RANGE_NAME = PureTeamList[i2]+"!A1"

        service = build('sheets', 'v4', credentials=credentials)

        body = {
        'values': values
        }

         # Update the sheet with the CSV data
        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()

        x = []
        y = []

        SERVICE_ACCOUNT_FILE = '/etc/secrets/GOOGLE_CREDENTIALS'
        credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes = ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/spreadsheets"]       
            )
        FOLDER_ID = '1_NGr0tLE9MJOWvjjHJo_U7-07iJfuhTj'  # Replace with your actual folder ID
        drive_service = build("drive", "v3", credentials=credentials)

        for i in range (TeamInstanceCount[PureTeamList[i2]]):
            x.append(Vault[PureTeamList[i2]+"a"+str(i)+"a"+str(0)])
            y.append(Vault[PureTeamList[i2]+"a"+str(i)+"a"+str(21)])

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Line')
        plt.xlabel('Match #')
        plt.ylabel('Total Points Scored')
        plt.title(str(PureTeamList[i2]))
        plt.legend()

        # Define the full path to save the image
        graph_path = os.path.join("public/data/ScouterGraphs", str(PureTeamList[i2]) + ".png")

        # Save the graph
        plt.savefig(graph_path, dpi=300)
        plt.close()  # Close the plot to free memory

        drive_service = build("drive", "v3", credentials=credentials)

            # Search for an existing file with the same name
        query = f"name='{PureTeamList[i2]}' and mimeType='image/png' and '{'1_NGr0tLE9MJOWvjjHJo_U7-07iJfuhTj'}' in parents"
        results = drive_service.files().list(q=query, fields="files(id)").execute()
        files = results.get("files", [])
        
        if files:
            # If file exists, update it
            file_id = files[0]['id']
            media = MediaFileUpload(graph_path, mimetype="image/png", resumable=True)
            drive_service.files().update(fileId=file_id, body={}, media_body=media).execute()
            print(f"Updated existing image: {PureTeamList[i2]}")
        else:
            # Otherwise, upload a new file
            file_metadata = {"name": PureTeamList[i2], "mimeType": "image/png"}
            media = MediaFileUpload(graph_path, mimetype="image/png")
            file = drive_service.files().create(body=file_metadata, media_body=media, fields="id, webContentLink").execute()
            file_id = file.get("id")

            # Make the file publicly accessible
            drive_service.permissions().create(
                fileId=file_id, body={"role": "reader", "type": "anyone"}
            ).execute()

        image_url = f"https://drive.google.com/uc?id={file_id}"

        spreadsheet = client.open("Battlecry")  # Open the existing spreadsheet
        worksheet = spreadsheet.worksheet(PureTeamList[i2])  # Select the sheet

        height = 300  # Adjust height as needed
        width = 500   # Adjust width as needed
        cell_range = "A13:E26"  # Define the range to merge (adjust as needed)

        # Merge the cells before inserting the image
        worksheet.merge_cells(cell_range)

        # Now insert the image formula
        worksheet.update(
            range_name='A13',
            values=[[f'=IMAGE("{image_url}", 4, {height}, {width})']],
            value_input_option="USER_ENTERED"
        )
    #The Jay Special:
    Jay0 = {}
    Jay1 = {}
    Jay2 = {}
    Jay3 = {}
    Jay4 = {}
    Jay5 = {}
    for i3 in range (len(PureTeamList)):
        teamFind = int(PureTeamList[i3])
        teamInstanceFind = 0
        for i in range (len(TeamList)):
            if str(teamFind) == str(TeamList[i]):
                teamInstanceFind = teamInstanceFind + 1
        totalPieces = 0
        climbCount = 0 
        processor = False
        net = False
        for j in range (teamInstanceFind):
            totalPieces = totalPieces+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(3)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(4)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(5)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(6)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(7)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(8)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(9)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(10)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(11)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(12)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(13)]))+int((Vault[str(teamFind)+"a"+str(j)+"a"+str(14)]))
            #this section is called exactly once for every team and every match that is logged for that team
            if (Vault[str(teamFind)+"a"+str(j)+"a"+str(17)] == "1") or (Vault[str(teamFind)+"a"+str(j)+"a"+str(16)] == "1"): 
                climbCount = climbCount + 1
            if (int(Vault[str(teamFind)+"a"+str(j)+"a"+str(13)]) > 0):
                processor = True
            if (int(Vault[str(teamFind)+"a"+str(j)+"a"+str(14)]) > 0):
                net = True

        pieceAverage = totalPieces/teamInstanceFind
        climbConsistency = ((int(climbCount)/int(teamInstanceFind)))*100//1
        Jay0[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]
        Jay1[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = str(teamFind)
        Jay2[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = str(pieceAverage)
        Jay3[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = str(climbConsistency)
        Jay4[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = processor
        Jay5[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000] = net
        ###Set the key to something directly related both to team number and epa: epa.team? What about 23.333?? 23.333.1058???????
        ###Then add EPA as a separate value to be written
        ###Jay1[Vault[str(teamFind)+"a"+str(teamInstanceFind-1)+"a"+str(29)]+teamFind/1000000]

        keyList = sorted(Jay1, key=Jay1.get, reverse=True)
        keyList.sort(reverse=True)
        with open ("public/data/TabData.csv", 'w') as file:
            #print (teamFind)
            file.write ("epic,equal,placeholder,climb,processor,net\nteam #,avg pieces scored,avg points scored,climb consistency %,can process?,can net?\n")
            for j1 in range (len(keyList)):
                #print(str(Jay1[keyList[j1]])+","+str(Jay2[keyList[j1]])+","+str(Jay0[keyList[j1]])+","+str(Jay3[keyList[j1]]))
                file.write(str(Jay1[keyList[j1]])+","+str(Jay2[keyList[j1]])+","+str(Jay0[keyList[j1]])+","+str(Jay3[keyList[j1]])+"%")
                if Jay4[keyList[j1]] == True:
                    file.write (",y,")
                else:
                    file.write (",n,")
                if Jay5[keyList[j1]] == True:
                    file.write ("y")
                else:
                    file.write ("n")
                file.write("\n")
        #this section is called exactly once for every individual team.
    tab = pd.read_csv('public/data/TabData.csv')
    tab = tab.fillna('')
    values = tab.values.tolist()

    RANGE_NAME = "Pick List"+"!A1"

    service = build('sheets', 'v4', credentials=credentials)

    body = {
    'values': values
    }

    # Update the sheet with the CSV data
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    x = []
    y = []

    SERVICE_ACCOUNT_FILE = '/etc/secrets/GOOGLE_CREDENTIALS'
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes = ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/spreadsheets"]       
        )
    FOLDER_ID = '1_NGr0tLE9MJOWvjjHJo_U7-07iJfuhTj'  # Replace with your actual folder ID
    drive_service = build("drive", "v3", credentials=credentials)

    keyList.sort()

    for j3 in range (len(keyList)):
        x.append(Jay2[keyList[j3]])
        y.append(keyList[j3])

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, marker='o')
    plt.xlabel('avg pieces scored')
    plt.ylabel('Total Points Scored')
    plt.title(str("pick list"))
    for i in range (len(x)):
        plt.text(x[i], y[i], Jay1[keyList[i]])
    
    # Define the full path to save the image
    graph_path = os.path.join("public/data/ScouterGraphs", "pickList" + ".png")

    # Save the graph
    plt.savefig(graph_path, dpi=300)
    plt.close()  # Close the plot to free memory

    drive_service = build("drive", "v3", credentials=credentials)

        # Search for an existing file with the same name
    query = f"name='pickList.png' and mimeType='image/png' and '{'1_NGr0tLE9MJOWvjjHJo_U7-07iJfuhTj'}' in parents"
    results = drive_service.files().list(q=query, fields="files(id)").execute()
    files = results.get("files", [])
        
    if files:
        # If file exists, update it
        file_id = files[0]['id']
        media = MediaFileUpload(graph_path, mimetype="image/png", resumable=True)
        drive_service.files().update(fileId=file_id, body={}, media_body=media).execute()
        print(f"Updated existing image: {PureTeamList[i2]}")
    else:
        # Otherwise, upload a new file
        file_metadata = {"name": PureTeamList[i2], "mimeType": "image/png"}
        media = MediaFileUpload(graph_path, mimetype="image/png")
        file = drive_service.files().create(body=file_metadata, media_body=media, fields="id, webContentLink").execute()
        file_id = file.get("id")
    
        # Make the file publicly accessible
        drive_service.permissions().create(
            fileId=file_id, body={"role": "reader", "type": "anyone"}
        ).execute()

    image_url = f"https://drive.google.com/uc?id={file_id}"

    spreadsheet = client.open("Battlecry")  # Open the existing spreadsheet
    worksheet = spreadsheet.worksheet('Pick List')  # Select the sheet

    height = 300  # Adjust height as needed
    width = 500   # Adjust width as needed
    cell_range = "G2:K15"  # Define the range to merge (adjust as needed)

    # Merge the cells before inserting the image
    worksheet.merge_cells(cell_range)

    # Now insert the image formula
    worksheet.update(
        range_name='G2',
        values=[[f'=IMAGE("{image_url}", 4, {height}, {width})']],
        value_input_option="USER_ENTERED"
    )

    ####Start of Auto V. Tele import

    graph_path = "public/data/ScouterGraphs/AutoVTele.png"
        # Search for an existing file with the same name
    query = f"name='AutoVTele.png' and mimeType='image/png' and '{'1_NGr0tLE9MJOWvjjHJo_U7-07iJfuhTj'}' in parents"
    results = drive_service.files().list(q=query, fields="files(id)").execute()
    files = results.get("files", [])
        
    if files:
        # If file exists, update it
        file_id = files[0]['id']
        media = MediaFileUpload(graph_path, mimetype="image/png", resumable=True)
        drive_service.files().update(fileId=file_id, body={}, media_body=media).execute()
        print(f"Updated existing image: {PureTeamList[i2]}")
    else:
        # Otherwise, upload a new file
        file_metadata = {"name": PureTeamList[i2], "mimeType": "image/png"}
        media = MediaFileUpload(graph_path, mimetype="image/png")
        file = drive_service.files().create(body=file_metadata, media_body=media, fields="id, webContentLink").execute()
        file_id = file.get("id")
    
        # Make the file publicly accessible
        drive_service.permissions().create(
            fileId=file_id, body={"role": "reader", "type": "anyone"}
        ).execute()

    image_url = f"https://drive.google.com/uc?id={file_id}"

    spreadsheet = client.open("Battlecry")  # Open the existing spreadsheet
    worksheet = spreadsheet.worksheet('Pick List')  # Select the sheet

    height = 300  # Adjust height as needed
    width = 500   # Adjust width as needed
    cell_range = "G17:K30"  # Define the range to merge (adjust as needed)

    # Merge the cells before inserting the image
    worksheet.merge_cells(cell_range)

    # Now insert the image formula
    worksheet.update(
        range_name='G17',
        values=[[f'=IMAGE("{image_url}", 4, {height}, {width})']],
        value_input_option="USER_ENTERED"
    )       
update ()