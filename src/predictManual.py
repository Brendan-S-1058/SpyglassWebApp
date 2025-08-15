import sys
import json

def Main ():
    inputR = sys.stdin.read()
    inputS = json.loads(inputR)

    #inputS = [1729,2423,5494,1073,69,6691,["2,6691,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,Algae removal/","2,4311,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,Got stuck on a ball most of the match/","2,10108,1,0,0,0,0,0,0,9,0,0,0,0,0,1,0,0,Medium cycles very consistent/","2,1512,1,0,0,0,0,0,0,0,0,2,3,0,0,0,0,1,nc/","2,6933,1,0,0,0,0,0,0,0,0,0,8,0,0,1,0,0,nc/","2,2262,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,Played some very light defense. attempted 1.5 auto/","3,9101,1,0,0,1,0,0,0,1,3,1,0,0,0,1,0,0,Can knock algae off/","3,10138,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Defense and just camped one source/","3,1073,1,0,0,0,1,0,0,0,2,2,2,0,0,0,0,1,Can knock algae/","3,839,1,0,0,0,2,0,0,0,4,4,4,0,0,1,0,1,nc/","5,3323,1,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,Can climb/","5,8421,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,Everything with coral is slow and inconsistent/","5,4572,1,1,0,0,0,0,0,0,0,0,0,2,0,0,0,1,Got to cage early to climb/","5,2423,1,0,0,0,3,0,0,1,5,5,1,0,0,0,0,1,Fast cycles and can knock algae has a unique L1 scoring system/","5,69,1,0,0,0,0,0,0,0,0,0,1,1,2,0,0,1,Only drove forward in auto/","6,811,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Very bad intake - very bad aim/","6,237,1,0,0,0,1,0,0,0,0,0,1,5,0,1,0,0,nc/","6,2523,1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,Train drive/","6,10108,1,0,0,0,0,0,0,7,0,0,0,0,0,1,0,0,nc/","6,1729,1,0,0,0,1,0,0,2,0,5,5,0,0,1,0,0,Algae removal/","6,4311,1,0,0,0,0,0,0,0,0,0,0,7,0,0,0,1,Exclusively processer and L1 takes a while for processing/","7,348,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Never moved/","7,166,1,0,0,0,1,0,0,0,2,4,3,2,0,1,0,1,nc/","7,9101,1,0,1,0,0,0,0,0,3,5,0,0,0,0,0,0,Algae removal/","7,5494,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,VERY inconsistent but can play defensive if need be/","7,6933,1,0,0,0,1,0,0,0,1,1,5,0,0,1,0,0,Strong and accurate auto alignment. Strong driving/","8,4572,1,0,0,0,1,0,0,0,0,5,0,0,0,0,0,0,nc/","8,2423,1,0,0,0,2,0,0,0,1,2,4,1,0,1,0,1,nc/","8,3323,1,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,nc/","8,4909,1,0,0,0,3,0,0,0,4,4,3,0,0,0,0,1,nc/","8,5687,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Pulled off field before match/","8,9096,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Disabled after auto/","9,7913,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Struggled with drive/","9,10138,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Defending/","9,8544,1,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,/","9,69,1,0,0,0,0,0,0,1,0,0,4,0,0,1,0,0,/","9,2523,1,0,0,0,0,0,0,0,2,3,0,0,0,1,0,0,A bit slow/","9,2262,1,0,0,0,0,0,0,1,0,0,4,0,0,0,0,0,Inconsistent with frequent coral drops/","11,5494,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Broke immediately-defense-very good-very close to deep climb/","11,1512,1,0,0,0,0,0,0,0,0,2,0,0,0,1,0,0,/","11,157,1,0,0,0,0,0,0,0,1,0,2,1,1,0,0,1,/","11,8421,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,/","11,1073,1,0,0,0,0,0,0,0,4,2,0,0,0,0,0,1,/","11,5687,0,0,0,0,2,0,0,5,0,3,4,1,0,0,0,1,Dey good/","12,8544,1,0,0,0,0,0,0,1,0,3,1,0,0,1,0,0,Algae removal -intelligent parking/","12,4311,1,1,0,0,0,0,0,0,0,0,0,8,0,0,0,1,Got stuck on algae for about ten seconds/","12,2423,1,0,0,0,2,0,0,1,4,1,3,0,0,1,0,0,/","12,2523,1,0,0,0,0,0,0,1,0,2,0,0,0,1,0,0,/","12,10138,1,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,/","12,9096,1,0,0,0,0,0,0,0,4,0,0,0,0,1,0,0,/","13,9101,1,1,0,0,0,0,0,0,3,3,0,0,0,1,0,0,Algae removal/","13,1729,1,0,0,0,0,0,0,0,0,1,6,0,0,1,0,0,Removed algae/","13,10066,1,1,0,0,0,0,0,4,0,0,0,0,0,1,0,0,Kit bot/","13,2262,1,0,0,0,0,0,0,0,1,0,4,0,0,1,0,0,/","13,4572,1,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,Failed climb/","13,348,1,0,0,0,0,0,0,0,1,6,0,0,0,1,0,0,/","14,3323,1,0,0,0,0,0,0,0,0,0,0,4,0,1,0,1,Algae removal/","14,10108,1,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,/","14,839,1,0,0,0,0,0,0,1,0,0,7,0,0,1,0,1,/","14,6933,1,0,0,0,1,0,0,0,0,6,1,0,0,1,0,0,Can knock algae also very consistent on all levels/","15,166,1,0,0,0,0,0,0,1,2,4,3,0,0,1,0,0,/","16,237,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,/","16,811,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,Defense after scoring one piece. Bad defense/","16,4909,1,0,0,0,3,0,0,0,0,4,8,0,0,0,0,1,/","16,6691,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,/","16,157,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,Good at algae/","17,10006,1,1,0,0,0,0,0,4,0,0,0,0,0,1,0,0,Good defense/","17,69,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,Broken -perchance -defense-unchallenged/","17,5494,1,0,0,0,0,0,0,0,0,1,5,0,0,1,0,0,/","17,10108,1,0,0,0,0,0,0,7,0,0,0,0,0,1,0,0,/","17,5687,1,0,0,0,2,0,0,0,5,7,3,1,1,1,0,0,/","17,1729,1,0,0,0,1,0,0,0,0,0,9,0,0,1,0,0,touchy small intake/","19,4909,1,0,0,0,3,0,0,0,5,6,4,0,0,0,0,1,No major problems/","19,6933,1,0,0,0,1,0,0,0,0,2,3,0,0,0,0,0,/","19,4311,1,1,0,0,0,0,0,0,0,0,0,9,0,0,0,1,/","20,157,1,0,0,0,0,0,0,1,1,0,0,0,2,0,0,1,/","20,839,1,0,0,0,2,0,0,1,3,3,2,0,0,0,0,1,/","20,2423,1,0,0,0,1,0,0,2,3,3,2,0,0,0,0,0,Unique L1 system/","20,6691,1,0,0,0,0,0,0,1,0,0,2,0,0,1,0,0,Very specific intake/","20,8544,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,/","20,1512,1,0,0,0,0,0,0,0,0,0,4,0,0,1,0,1,/","21,9096,1,0,0,0,0,0,0,3,3,2,0,0,0,1,0,0,Nice park/","22,7913,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,Back left swerve module not working. No deep chage/","21,237,1,0,0,0,0,0,0,1,0,0,3,2,0,1,0,0,/","21,2262,1,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,/","21,3323,1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,1,/","21,1073,1,0,0,0,0,0,0,0,0,1,5,0,0,1,0,1,/","22,1729,1,0,0,0,1,0,0,0,1,2,6,0,0,0,0,0,/","22,4572,1,0,0,0,1,0,0,3,0,0,0,0,0,1,0,0,Only focused on L1/","22,10108,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,Can play defensive but not well enough for benefits/","22,5687,1,0,0,0,3,0,0,0,6,6,2,0,2,0,0,1,nc/","24,166,1,0,0,0,0,0,0,0,4,6,3,0,0,0,0,1,/","24,10138,1,1,0,0,0,0,0,7,0,0,0,0,0,0,0,0,/","24,6691,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,Tipped after 15 seconds/","25,10066,1,1,0,0,0,0,0,7,0,0,0,0,0,1,0,0,Surprisingly good/","25,8544,1,0,0,0,0,0,0,0,3,0,0,2,0,1,0,0,Good alage/","25,237,1,0,0,0,1,0,0,0,0,0,0,3,0,1,0,0,/","25,4572,1,0,0,0,1,0,0,1,0,0,2,0,0,0,0,0,Failed climb/","25,7913,0,0,0,0,0,0,0,3,1,2,0,0,0,1,0,0,/","25,348,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,/","26,839,1,0,0,0,2,0,0,0,0,2,6,0,0,0,0,1,Quick climb can do alage/","26,2423,1,0,0,0,1,0,0,1,3,5,2,0,0,1,0,0,/","26,1512,1,0,0,0,1,0,0,0,0,2,0,0,0,1,0,0,Drive problems the whole time/","26,811,1,0,0,0,0,0,0,0,2,1,0,0,0,1,0,0,/","26,9101,1,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,/","28,8544,1,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,Bad intake - bad shooter/","28,166,1,0,0,0,1,0,0,0,0,2,11,0,0,1,0,0,/","28,157,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,/","29,6933,0,0,0,0,2,0,0,0,0,1,5,0,0,0,0,0,Full match spent on coral/","29,1729,1,0,0,0,1,0,0,2,0,2,4,0,0,1,0,1,/","29,2523,1,0,0,0,0,0,0,0,3,2,1,0,0,0,0,0,Still train drive/","29,3323,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,/","29,811,1,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,/","29,1512,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,/","30,4311,1,1,0,0,0,0,0,0,0,0,0,7,0,0,0,1,Insane/","30,348,1,0,0,0,0,0,0,0,1,5,0,0,0,1,0,0,/","30,5687,1,0,0,0,3,0,0,0,3,5,7,4,0,0,0,0,Stuck on algae for last 15 seconds/","30,4909,1,0,0,0,2,0,0,1,0,0,10,0,0,0,0,1,/","30,2423,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,0,/","30,8421,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,/","31,839,0,0,0,0,2,0,0,0,5,3,2,0,0,0,0,1,Missed a few shots/","31,4572,1,0,0,0,1,0,0,6,1,0,0,0,0,0,0,0,/","31,2262,1,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,/","31,10108,1,1,0,0,0,0,0,7,0,0,0,0,0,1,0,0,/","31,10066,1,0,0,0,0,0,0,5,0,0,0,0,0,1,0,0,Tried new auto/","31,1073,1,0,0,0,2,0,0,0,3,2,2,0,0,1,0,1,/","32,9096,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,/","32,69,1,0,0,0,0,0,0,0,2,0,4,0,0,0,0,0,/","32,9101,1,0,1,0,0,0,0,1,4,3,6,0,0,0,0,0,Can knock algae. Can climb values coral/","32,10138,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,/","32,7913,0,0,0,0,0,0,0,2,1,2,0,0,0,1,0,0,/","34,8544,1,0,0,0,0,0,0,0,1,0,0,2,0,1,0,0,Flipped/","34,4909,1,0,0,0,3,0,0,0,1,5,7,0,0,0,0,1,/","34,8421,1,0,0,0,0,0,0,0,0,0,0,3,0,1,0,0,/","34,2523,1,0,0,0,0,0,0,1,3,4,0,0,0,1,0,0,/","34,10108,1,1,0,0,0,0,0,7,0,0,0,0,0,1,0,0,/","34,839,0,0,0,0,1,0,0,0,3,3,6,0,0,0,0,1,Pretty consistent/","35,6691,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,Defended in late game still a bad intake though/","35,1073,1,0,0,0,2,0,0,0,3,3,4,0,0,1,0,1,/","35,5494,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1,/","35,1729,1,0,0,0,0,0,0,2,2,2,0,0,0,1,0,0,/","35,2423,1,0,0,0,2,0,0,1,4,3,4,0,0,1,0,0,Can't climb. Fast and consistent cycles/","35,69,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,/","36,10066,1,0,0,0,1,0,0,6,0,0,0,0,0,1,0,0,Missed two L1s/","36,6933,1,0,0,0,1,0,0,0,2,0,6,0,0,1,0,0,/","36,10138,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,Defense after auto. Very good defense but only on 1 source/","36,157,1,0,0,0,0,0,0,1,1,3,3,0,0,0,0,1,/","36,4572,1,0,0,0,1,0,0,3,0,0,4,0,0,0,0,1,/","37,2262,1,0,0,0,0,0,0,1,0,1,6,0,0,0,0,0,/","37,811,1,1,0,0,0,0,0,0,0,0,5,0,0,1,0,0,Bad intake -defendable/","37,3323,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Broken/","37,9096,1,0,0,0,0,0,0,0,1,2,0,0,0,1,0,0,Defense for first minute/","38,9101,1,1,0,0,0,0,0,0,0,4,4,0,0,1,0,0,Algae removal decent/","38,4909,1,0,0,0,2,0,0,0,1,0,2,0,0,0,0,1,3 peice auto potential/","38,4311,1,1,0,0,0,0,0,0,0,0,0,7,0,0,0,1,/","39,4572,1,0,0,0,1,0,0,0,0,0,4,0,0,0,0,0,Started Browning out - too inconsistent?/","39,6691,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,intake not working?/","39,348,1,0,0,0,0,0,0,0,2,4,0,0,0,1,0,0,Can take off low algae/","39,2523,1,0,0,0,0,0,0,0,1,2,0,0,0,1,0,0,/","40,10066,1,1,0,0,0,0,0,6,0,0,0,0,0,1,0,0,Hard to time for human player/","40,9096,1,0,0,0,0,0,0,0,4,3,0,0,0,0,0,0,Can't climb/","40,10066,1,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,Potential for 2 piece L1 auto. Looking like best rookie bot/","41,1073,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,Broke for most of match/","41,2423,1,0,0,0,2,0,0,0,2,3,3,1,0,1,0,1,/","41,2423,1,0,0,0,2,0,0,0,2,3,5,1,0,0,0,1,Unique climber. Almost 3 peice auto algae capabilities/","3,2370,1,1,0,0,0,0,0,0,0,2,6,2,0,0,1,0,Algae dislodge in auto. Human player feeding can be finicky/","7,2370,1,0,0,0,0,0,0,0,0,0,7,2,0,0,0,1,nc/","16,2370,1,0,0,0,0,0,0,1,0,0,7,0,0,1,0,0,Auto missed/","26,2370,1,0,0,0,1,0,0,0,1,1,6,0,2,0,0,1,Cool barge shooting/","32,2370,0,0,0,0,1,0,0,0,2,3,1,4,0,0,0,1,Co-op bonus/","36,2370,1,0,0,0,0,0,0,2,4,3,2,0,0,0,0,0,3 peice auto potential.  Scores in others processer. Unique scoring. Can climb chose not to. HIGH POTENTIAL/","39,2370,1,0,0,0,2,0,0,0,0,1,8,0,0,0,0,1,Durable/","5,95,1,0,0,0,3,0,0,0,0,0,7,0,0,1,0,1,nc/","10,95,1,0,0,0,2,0,0,2,0,0,6,0,0,0,0,1,/","24,95,1,0,0,0,2,0,0,0,0,0,7,0,0,0,0,1,Good at a lot/","37,95,1,0,0,0,3,0,0,4,0,0,3,0,0,0,0,0,Corner Deep Cage attempt. Ground intake/","41,95,1,0,0,0,2,0,0,3,0,0,7,0,0,1,0,0,/","1000,95,1,0,0,0,3,0,0,2,0,0,7,0,0,0,0,0,nc/","4,1058,1,0,0,0,0,0,0,2,0,0,3,0,1,0,0,1,Zoinkers/","10,1058,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,Tipped/","15,1058,1,1,0,0,0,0,0,0,0,1,1,2,0,0,0,1,Only ran algae/","18,1058,1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1,Something is very wrong/","23,1058,1,0,0,0,0,0,0,1,0,0,5,1,0,1,0,0,Smart driving/","27,1058,0,1,0,0,0,0,0,3,1,0,3,1,0,0,0,0,Close to climb/","33,1058,1,0,0,0,0,0,0,2,0,0,4,0,0,0,0,0,Almost a climb/","42,1058,1,0,0,0,1,0,0,2,1,3,4,0,0,0,0,1,PEAK/","50,1058,1,0,0,0,2,0,0,0,0,0,7,0,0,1,0,0,Algae removal/"]]

    count = 0
    holdList = []
    hold = ''
    for char in inputS:
        if char != ",":
            hold += char
        else:
            if count < 6:
                holdList.append(hold)
                count += 1
                hold = ''
            else:
                hold += char
    holdList.append(hold)
    inputS = holdList

    rList = search (inputS)
    #print ('rList: ' + str(rList), file = sys.stderr)

    relevantDict = rList[0]
    keyList = rList [1]

    del rList

    #breaks matches from string to lists -- REMOVES COMMENTS
    for key in keyList:
        allmatches = []
        for match in relevantDict[key]:
            hold = ''
            matchList = []
            for char in match:
                if char != ',':
                    hold += (char)
                else:
                    matchList.append(hold)
                    hold = ''
            allmatches.append(matchList)
        relevantDict[key] = allmatches
    #print ('relevantDict: ' + str(relevantDict), file=sys.stderr)
    for key in keyList:
        match_numbers = []
        for match in relevantDict[key]:
            #print (match)
            match_numbers.append (match[0])
        match_numbers.sort()
        relevantDict[str(key)+"matches"] = match_numbers

    averageMatches = []
    for key in keyList:
        teamHoldList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #divisor = 0
        countmatches = 0
        for match in relevantDict[key]:
            count = 0
            countmatches += 1
            #all these comments are for trying to weight later matches more, but a: it's not working, and b: I don't think it adds accuracy
            #recent = relevantDict[str(key) + "matches"].index(match[0])/len(relevantDict[str(key) + "matches"])
            #divisor += recent
            for item in match:
                count += 1
                if count > 2:
                    teamHoldList[count-1] += (int(item))
                    #teamHoldList[count-1] += (int(item)*recent)
        #print (teamHoldList)
        for i in range(len(teamHoldList)):
            teamHoldList[i] /= countmatches
            #teamHoldList[i] /= divisor
        #print (teamHoldList)
        averageMatches.append (teamHoldList)
    blueAverageMatchUnprocessed = []
    redAverageMatchUnprocessed = []
    for i in range (len(averageMatches[0])-2):
        blueAverageMatchUnprocessed.append(averageMatches[0][i+2]+averageMatches[1][i+2]+averageMatches[2][i+2])
        redAverageMatchUnprocessed.append(averageMatches[3][i+2]+averageMatches[4][i+2]+averageMatches[5][i+2])
    
    blueStart = calc(blueAverageMatchUnprocessed)
    redStart = calc(redAverageMatchUnprocessed)

    blueAverageMatchHalfProcessed = cap(blueAverageMatchUnprocessed)
    redAverageMatchHalfProcessed = cap(redAverageMatchUnprocessed)

    blueFinal = calc (blueAverageMatchHalfProcessed)
    redFinal = calc (redAverageMatchHalfProcessed)

    result = analyze(blueFinal, redFinal, blueStart, redStart)

    print (json.dumps(result))

    #start getting every score from each match and returning it to the scores list, maybe record locations of score - cap an auto - cap algae - so on so forth


#searches actually by team# rather than something else (if in)
def search (inputS):
    teams = [int(inputS[0]), int(inputS[1]), int(inputS[2]), int(inputS[3]), int(inputS[4]), int(inputS[5])]
    data = inputS[6]

    #print ('data:' + str(data), file=sys.stderr)
    
    holdList = []
    hold = ''
    after = True
    for char in data:
        if char == "," and after == True:
            after = False
        elif char != '[' and char != ']' and char != '\"' and char != '/':
            hold += char
            after = False
        elif char == '/':
            holdList.append(hold+char)
            hold = ''
            after = True
    
    data = holdList
    #print ('data: ' + str(data), file = sys.stderr)

    del hold
    del holdList
    del after

    sorted = {}

    for team in teams:
        sorted[team] = []

    for item in data:
        #print ('item: ' + str(item), file=sys.stderr)
        ccount = 0
        allcount = 0
        team = ''
        for char in item:
            if ccount < 2:
                if char == ',':
                    ccount += 1
                elif ccount == 1:
                    team += char
                if ccount >= 2:
                    #print ('team: ' + str(team), file=sys.stderr)
                    if int(team) in teams:
                        sorted[int(team)].append(item)
                    team = ''

                allcount += 1

    return ([sorted, teams])

def cap (match):

    #one can assume that the average match from which scouting data is pulled is not a particularly good composition, so one must give to good matches as one takes away from bad matches
    x = (match[1] + match[2] + match[3] + match[4] + match[7] + match[8] + match[9] + match[10])

    if ((match[5] + match[6] + match[11] + match[12]/(x/4+(4/x)**(x/3)-1))>0.85 and (match[5] + match[6] + match[11] + match[12]/(x/4+(4/x)**(x/3)-1))<1.1) or (match[5] + match[6] + match[11] + match[12]) > 9:
        match[7] += 0.7
        match[8] += 0.7
        match[9] += 0.7
        match[10] += 0.7
    
    if match[1] > 5:
        match[1] = 5 + (match[1]-5)*0.5
    if match[2] > 5:
        match[2] = 5 + (match[2]-5)*0.75 
    if match[3] > 6:
        match[3] = 6 + (match[3]-8)*0.75
    if match[4] > 12:
        match[4] = 12
    if match[5] > 3:
        match[5] = 3
    if match[6] > 3:
        match[6] = 3
    if match[7] > 14:
        match[7] = 14 + (match[7]-14)*0.5
    if match[8] > 12:
        match[8] = 12
    if match[9] > 12:
        match[9] = 12
    if match[10] > 12:
        match[10] = 12
    if match[11] > 9:
        match[11] = 9
    if match[12] > 9:
        match[12] = 9

    coralavg = (match[1] + match[2] + match[3] + match[4] + match[7] + match[8] + match[9] + match[10])/4

    if (match[1] + match[7]) > coralavg - 1.5 and (match[1] + match[7]) < 1.5 + coralavg:
        print ('akb')
        if match[7] > 0.05:
            match[7] += 0.4
    
    if (match[2] + match[8]) > coralavg - 1.5 and (match[2] + match[8]) < coralavg + 1.5:
        print ('akn')
        if match[8] > 0.05:
            match[8] += 0.3
    
    if (match[3] + match[9]) > coralavg - 1.5 and (match[3] + match[9]) < 1.5 + coralavg:
        print ('aghd')
        if match[7] > 0.05:
            match[7] += 0.4
    
    if (match[4] + match[10]) > coralavg - 1.5 and (match[4] + match[10]) < coralavg + 1.5:
        print ('javb')
        if match[10] > 0.05:
            match[10] += 0.6
    
    increment = 0
    bar = 9 
    while match[5] + match[6] + match[11] + match[12] + increment < (match[1] + match[2] + match[3] + match[4] + match[7] + match[8] + match[9] + match[10])/6: 
        if match[8] > bar:
            match[8] -= 0.25
            increment += 0.25
        elif match[7] > bar:
            match[7] -= 0.25
            increment += 0.3
        elif match[9] > bar:
            match[9] -= 0.15
            increment += 0.25
        elif match[10] > bar:
            match[10] -= 0.4
            increment += 0.3
        else:
            bar -= 1
        if match[11] > 0:
            match[11] += 0.2
        if match[12] > 0:
            match[12] += 0.5
    
    if match[1] + match[7] > 12:
        match[7] -= match[7] + match[1] - 12
    if match[2] + match[8] > 12:
        match[8] -= match[8] + match[2] - 12
    if match[3] + match[9] > 12:
        match[9] -= match[9] + match[3] - 12
    if match[4] + match[10] > 12:
        match[10] -= match[10] + match[4] - 12
    
    while match[5] + match[6] + match[11] + match[12] > 9:
        match[11] -= 0.5
        match[12] -= 0.5

    return (match)

def calc (match):
    score = 0
    score += (match[0]*3)+(match[1])*3+(match[2])*4+(match[3])*6+(match[4])*7+(match[5])*2+(match[6])*4
    score += (match[7])*2+(match[8])*3+(match[9])*4+(match[10])*5+(match[11])*2+(match[12])*4
    if ((match[13])*2+(match[14])*6+(match[15])*12) > 36:
        score += 36
    else:
        score += (match[13])*2+(match[14])*6+(match[15])*12
    
    return (score)

def analyze (bscore, rscore, bstart, rstart):
    bstate = bscore-rscore

    mod = 0
    if bstate > 0:
        bwin = True
        deci = (bscore-rscore)/bscore
        gauge = 0
        mod = 0
        while deci > gauge:
            mod += 1
            gauge = mod/500
        #print (mod)
        rp = (250-mod)/5
        bp = (250+mod)/5
        if bp>=100:
            bp = 99.99
            rp = 0.01

    else:
        bwin = False
        deci = (rscore-bscore)/rscore
        gauge = 0
        mod = 0
        while deci > gauge:
            mod += 1
            gauge = mod/500
        #print (mod)
        bp = (250-mod)/5
        rp = (250+mod)/5
        if rp>=100:
            rp = 99.99
            bp = 0.01
    
    if bscore>bstart:
        bscore = str(bstart-5) + '-' + str(bscore+5)
    else:
        bscore = str(bscore-5) + '-' + str(bstart+5)

    if rscore>rstart:
        rscore = str(rstart-5) + '-' + str(rscore+5)
    else:
        rscore = str(rscore-5) + '-' + str(rstart+5)
    

    
    return [bwin, bscore, rscore, bp, rp]

Main ()