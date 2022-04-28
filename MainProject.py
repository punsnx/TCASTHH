from asyncore import loop
from re import S
from secrets import choice
from statistics import median
import pandas as pd 
import numpy
import statistics

df = pd.read_csv("foodkakkak.csv")
df.dropna(inplace = True)
checkUser = 0
def findChoice(compareTime,CurTemp) :
    # LIST D0=Row, D1=Name_TH, D2=RATE, D3=Temperature, D4=Kind
    list = [[],[],[],[],[]]
    # LIST USEFUL FOOD PASS >> JUNK & USEFUL
    # D0=Temperature, D1=RATE, D2=KIND 
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
        if Choice[0] ==
    return Choice

askWant = str(input("Do you want something? : "))
if askWant.casefold() == "yes" :
    print("OK Input Next!")
    print("<Now enter your current time>")
    print("use this format!", "24 hours time format!")
    print("01:00AM")
    askTime = str(input("Current Time : "))

    print("<Now enter your current temperature>")
    print("use this format!", "Celcieus!")
    print("35")
    askTemp = int(input("Current Temperature : "))

    print("<Now enter your current weather>")
    print("use this format!", "SELECT from number")
    print("1 Clear =แจ่มใส\n2 Dry =แห้ง\n3 Sweltering =ร้อนระอุ\n4 Sunny =แดดจัด\n5 Frosty =หนาวจัด\n6 Cold =เย็น\n7 Stormy =มีพายุ\n8 Breezy =มีลมอ่อน\n9 Windy =ลมแรง\n10 Misty =มีหมอก\n11 Cloudy =มีเมฆมาก\n12 Rainy =ที่ฝนตก")
    print("If your weather is Clear >> Type 1")
    askWeather = int(input("Current Weather : "))
    print(askTime, askTemp, askWeather)

    while True :
        print("USE This Format! for Select match passed choices!")
        print("1 = Temperature, RATE and Kind PASSED\n2 = Tempertature and RATE PASSED \n3= Temperature PASSED")
        askFood = int(input("SELECT FOOD : "))
        if askFood < 4 and askFood > 0 :
            if runFromUserChoose(askTime,askTemp,askFood) 
            
else :
    print("Hope you come back! ;)")