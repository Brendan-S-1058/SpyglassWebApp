import pandas as pd
import os
import matplotlib.pyplot as plt
import statbotics
import sys
import json
import gspread

def Main ():
    global Vault
    global TeamList
    global countb
    export_import_data = ""
    countd = 0
    DOUBLE = True
    input = sys.stdin.read()

    for char in input:
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
    
    state = False
    NewSheet (state)


    result = {export_import_data}
    print(json.dumps(result))

Main ()