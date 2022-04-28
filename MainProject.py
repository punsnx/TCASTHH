import pandas as pd 

df = pd.read_csv("foodkakkak.csv")

def mainAlgorithm():
    # Row Name Rate Temp
    list = [[],[],[],[]]
    if "AM" in str(askTime) :
        print("AM YES")
        for i in df.index :
            if "AM" in str(df.loc[i, "DATE_TIME"]) :
                print("YES AM WOW")
    elif "PM" in str(askTime) :
        print("PM YES")
        for i in df.index :
            if "PM" in str(df.loc[i, "DATE_TIME"]) :
                print("YES PM WOW")



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

    mainAlgorithm()
else :
    print("SAD")