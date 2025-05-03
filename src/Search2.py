

def Main ():
    inputR = sys.stdin.read()
    inputS = str(json.loads(inputR))
    dataLists = []
    holdList = []
    hold = ""

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

    for char in export_import_data:
        if char != "," and char != "/" and char != "\n" and char != "\"":
            hold += char 
        if char == ",":
            holdList.append(hold)
            hold = ""
        elif char == "/":
            dataLists.append(holdList)
            holdList = []



    

Main ()
print (json.dumps(arrayR))