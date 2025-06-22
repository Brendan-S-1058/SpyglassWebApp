import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputI = json.loads(inputR)

    print ('inputR: ' + str(inputR), file=sys.stderr)

    if inputI == "1":
        Public ()
    else:
        Local (inputI)

def Public ():
    with open("public/data/Public.txt","r") as f:
        rawData = f.read()
        f.close()
    print ("public input: " + str(rawData), file=sys.stderr)
    qqq = SortAndReturn (rawData)
    

def Local (datain):
    start = True
    dataout = ''
    for char in  datain:
        if char == ',' and start == True:
            start = False
        elif start == False:
            dataout += char
    
    #should remove leading mode value and first comma

    print ("inputI: " + str(dataout), file=sys.stderr)





'''
    DataValue = ""
    dataList = []
    counta = 0
    moreData = False
    countc = 0
    leftovers = ""

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
                linebreak = True'''


def SortAndReturn (rawData):
    return rawData 
'''
1: figure out input - (-1,,1,1058,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment/,100,1058,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool/,100,3467,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool/) or (1  1058,1,1,2,1,2,4,1,1,4,4,4,4,1,1,0,0,1,No comment,,1058,100,1,0,0,0,2,1,0,0,1,3,7,3,4,0,0,1,Pretty cool,,3467,100,1,0,0,0,1,1,0,0,1,3,3,3,4,0,0,1,Pretty cool,,)
2: figure out intended output - (start at avg points scored per team)
3: make a structure to convert input to output in both cases
4: make it sortable by multiple modes
'''

Main ()

print (json.dumps("NOT DONE YET"))