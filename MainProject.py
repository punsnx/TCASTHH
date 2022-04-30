import pandas as pd 
import numpy
import statistics
import random
import sys
df = pd.read_csv("foodkakkak.csv")
df.dropna(inplace = True)
def findChoice(compareTime,CurTemp) :
    # LIST D0=Row, D1=Name_TH, D2=RATE, D3=Temperature, D4=Kind
    list = [[],[],[],[],[]]
    # LIST USEFUL FOOD PASS >> JUNK & USEFUL
    # D0=ONLY_Date_Passed, D1=TEMP_Passed, D2=TEMP_RATE_Passed , D3=ALL_PASSED
    foruse = [[],[],[],[]]
    #PART CHECK TIME
    #NO JUNK REUSE FOR TIME CHECK
    if compareTime == "AM" :
        for i in df.index :
            if int(df.loc[i, "DATE_TIME"][11:13]) < 12 :
                list[0].append(i)
                list[1].append(df.loc[i, "Name_TH"])
                list[2].append(df.loc[i, "RATE"])
                list[3].append(df.loc[i, "Temperature"])
                list[4].append(int(str(df.loc[i, "Kind"])[0]))
    elif compareTime == "PM" :
        for i in df.index :
            if int(df.loc[i, "DATE_TIME"][11:13]) >= 13 :
                list[0].append(i)
                list[1].append(df.loc[i, "Name_TH"])
                list[2].append(df.loc[i, "RATE"])
                list[3].append(df.loc[i, "Temperature"])
                list[4].append(int(str(df.loc[i, "Kind"])[0]))
    #PART CHECK CHOICE
    for j in range(len(list[0])) :
        #VAR MOST COMMON KIND OF FOOD [timeTrue]
        npyMeanL2 = int(numpy.mean(list[2]))
        #TEMPERATURE CHECK >> IN RANGE USER +-4
        if list[3][j] in range(CurTemp,CurTemp-4,-1) or list[3][j] in range(CurTemp,CurTemp+4,1) :
            #RATE CHECK IN RANGE MODE +5 / -2
            if list[2][j] in range(npyMeanL2,npyMeanL2+6,1) or list[2][j] in range(npyMeanL2,npyMeanL2-3,-1) :
                #CHECK COMMON KIND 
                if list[4][j] == statistics.mode(list[4]) :
                    #FOR YUMMY FOOD
                    foruse[3].append(list[0][j])
                #FOR REUSE KIND [NOT PASS] 
                else :
                    foruse[2].append(list[0][j])
            #FOR REUSE RATE [NOT PASS] 
            else :
                foruse[1].append(list[0][j])
        #FOR REUSE TEMP [NOT PASS] 
        else :
            foruse[0].append(list[0][j])
    return foruse
def runFromUserChoose(time,CurrentTemp,userSelected):
    if "AM" in str(time) :
        Choice = findChoice("AM",CurrentTemp)
    elif "PM" in str(time) :
        Choice = findChoice("PM",CurrentTemp)
    if userSelected == 1 :
        if Choice[3] != [] :
            r = random.choice(Choice[3])
            return r
        else :
            r = "null"
            return r
    elif userSelected == 2 :
        if Choice[2] != [] :
            r = random.choice(Choice[2])
            return r
        else :
            r = "null"
            return r
    elif userSelected == 3 :
        if Choice[1] != [] :
            r = random.choice(Choice[1])
            return r
        else :
            r = "null"
            return r
    elif userSelected == 4 :
        if Choice[0] != [] :
            r = random.choice(Choice[0])
            return r
        else :
            r = "null"
            return r

askWant = str(input("Do you want something? [YES/NO] : "))
if askWant.casefold() == "yes" :
    print("-----------------------------------------------\nOK Next!\n-----------------------------------------------")
    print("<Now enter your current time>\nFormt Example!\n01:00AM")
    print("-----------------------------------------------")
    askTime = str(input("Current Time : "))
    print("-----------------------------------------------")
    print("<Now enter your current temperature>\nuse this format!", "Celcieus!\nExample 35 >> means 35 degree celcieus!")
    print("-----------------------------------------------")
    askTemp = int(input("Current Temperature : "))
    print("-----------------------------------------------")
    print("<Now enter your current weather>\nuse this format!", "SELECT from number")
    print("1 Clear =แจ่มใส\n2 Dry =แห้ง\n3 Sweltering =ร้อนระอุ\n4 Sunny =แดดจัด\n5 Frosty =หนาวจัด\n6 Cold =เย็น\n7 Stormy =มีพายุ\n8 Breezy =มีลมอ่อน\n9 Windy =ลมแรง\n10 Misty =มีหมอก\n11 Cloudy =มีเมฆมาก\n12 Rainy =ที่ฝนตก")
    print("Example >> If your weather is Clear >> Type 1")
    print("-----------------------------------------------")
    askWeather = int(input("Current Weather : "))
    print("-----------------------------------------------\nOverview your info!\n-----------------------------------------------")
    print(askTime, askTemp, askWeather)
    print("-----------------------------------------------")
    while True :
        print("-----------------------------------------------\nOrder Me!\n-----------------------------------------------")
        print("USE This Format! for Select match passed choices!")
        print("1 = Temperature, RATE and Kind PASSED\n2 = Tempertature and RATE PASSED \n3= Temperature PASSED\n4=Time PASSED\n5=EXIT")
        print("-----------------------------------------------")
        askFood = int(input("SELECT FOOD : "))
        print("-----------------------------------------------\nGet it!\n-----------------------------------------------")
        if askFood < 5 and askFood > 0 :
            cRow = runFromUserChoose(askTime,askTemp,askFood)
            if cRow != "null" :
                print(cRow)
                Answer = "ชื่อภาษาไทย : {0}\nName : {1}\nKind : {2}\nRate : {3}\nReview : {4}\nMood : {5}\nDate & Time : {6}\nWeather : {7}\nTemperature : {8}"
                print(Answer.format(df.loc[cRow][1],df.loc[cRow][2],df.loc[cRow][3],df.loc[cRow][4],df.loc[cRow][5],df.loc[cRow][6],df.loc[cRow][7],df.loc[cRow][8],df.loc[cRow][9]))
                print("-----------------------------------------------")
                askLike = str(input("Do you like it? [YES/NO] : "))
                if askLike.casefold() == "yes" :
                    print("-----------------------------------------------\nTHANKS\n-----------------------------------------------")
                    break
                elif askLike.casefold() == "no" :
                    askTryAgain = str(input("Do you want to try again? [YES/NO] : "))
                    if askTryAgain.casefold() == "yes" :
                        print("TRY AGAIN!\n-----------------------------------------------")
                        continue
                    elif askTryAgain.casefold() == "no" :
                        print("SORRY!")
                        print("-----------------------------------------------\nTHANKS\n-----------------------------------------------")
                        break
            else :
                print("Data not available! TRY AGAIN!")
        elif askFood == 5 :
            print("-----------------------------------------------\nTHANKS\n-----------------------------------------------")
            break
        else :
            print("ERROR : SELECT FOOD not vild! Try Again")
            continue        
else :
    print("Hope you come back! ;)")

sys.exit