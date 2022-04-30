from tkinter import *
from tkinter.ttk import *
import pandas as pd 
import numpy
import statistics
import random
import requests
from bs4 import BeautifulSoup
import io
import urllib
from PIL import Image, ImageTk

app = Tk()
app.title("Do you want something to eat?")
app.geometry('1600x900')
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
def start_btn_clicked() :
    start_btn.grid_forget()
    txt_dsi.grid(column=0, row=1)
    txt_dsi_time.grid(column=0, row=2)
    txt_dsi_temp.grid(column=0, row=3)
    txt_dsi_weather.grid(column=0, row=4)

    dsi_time.grid(column=1, row=2)
    dsi_temp.grid(column=1, row=3)
    dsi_weather.grid(column=1, row=4)
    dsi_submit_btn.grid(column=1, row=5)
fontSet = "FC Marshmallow Brush"
lbl = Label(app, text="Do you want something to eat?", font=(fontSet, 90))
start_btn = Button(app, text="START", command=start_btn_clicked)
#dsi = data start input!!
txt_dsi = Label(app, text="Please enter your info!", font=(fontSet, 50))
txt_dsi_time = Label(app, text="Enter your current TIME Example [01:00AM] ", font=(fontSet, 40))
txt_dsi_temp = Label(app, text="Enter your current TEMPERATURE Example [36] ", font=(fontSet, 40))
txt_dsi_weather = Label(app, text="Enter your current WEATHER [click to Select] ", font=(fontSet, 40))

dsi_time = Entry(app,width=20)
dsi_temp= Entry(app,width=20)
dsi_weather = Combobox(app)
dsi_weather['values']= ("1 Clear = แจ่มใส","2 Dry = แห้ง","3 Sweltering = ร้อนระอุ","4 Sunny = แดดจัด","5 Frosty = หนาวจัด","6 Cold = เย็น","7 Stormy = มีพายุ","8 Breezy = มีลมอ่อน","9 Windy = ลมแรง","10 Misty = มีหมอก","11 Cloudy = มีเมฆมาก","12 Rainy = ที่ฝนตก")
dsi_weather.current(0) #set the selected item

def dsi_submit_btn_clicked() :
    txt_dsi.grid_forget()
    txt_dsi_time.grid_forget()
    txt_dsi_temp.grid_forget()
    txt_dsi_weather.grid_forget()

    dsi_time.grid_forget()
    dsi_temp.grid_forget()
    dsi_weather.grid_forget()
    dsi_submit_btn.grid_forget()
    if len(dsi_time.get()) == 0 or len(dsi_temp.get()) == 0 or len(dsi_weather.get()) == 0:
        start_btn_clicked(0)
    else :
        global Data_time, Data_Temp, Data_Weather
        Data_time = dsi_time.get()
        Data_Temp =  int(dsi_temp.get())
        Data_Weather  = dsi_weather.get()
        showUserAsk(0)
dsi_submit_btn = Button(app, text="SUBMIT", command=dsi_submit_btn_clicked)

selected = IntVar()
#uso = user select output 
uso_txt = Label(app,text="Select sorting level!")
uso_select1 = Radiobutton(app,text='1 = Temperature, RATE, Kind and Time PASSED', value=1, variable=selected)
uso_select2 = Radiobutton(app,text='2 = Tempertature and RATE PASSED', value=2, variable=selected)
uso_select3 = Radiobutton(app,text='3= Temperature PASSED', value=3, variable=selected)
uso_select4 = Radiobutton(app,text='4= Time PASSED', value=4, variable=selected)
uso_select5 = Radiobutton(app,text='5=EXIT', value=5, variable=selected)
uso_state_txt = Label(app,text="")


def usoClicked() :
    global cRowShow, Answer, showAnswer, askLike, like_yes, like_no, OutIMG1, OutIMG2, OutIMG3
    if selected.get() < 6 and selected.get() > 0 :
        cRow = runFromUserChoose(Data_time,Data_Temp,selected.get())
        if selected.get() == 5 :
            app.destroy()
        elif cRow != "null" :
            hideUserAsk()
            cRowShow = Label(app, text=cRow)
            cRowShow.grid(column=0, row=1)
            Answer = "ชื่อภาษาไทย : {0}\nName : {1}\nKind : {2}\nRate : {3}\nReview : {4}\nMood : {5}\nDate & Time : {6}\nWeather : {7}\nTemperature : {8}"
            showAnswer = Label(app,text=Answer.format(df.loc[cRow][1],df.loc[cRow][2],df.loc[cRow][3],df.loc[cRow][4],df.loc[cRow][5],df.loc[cRow][6],str(df.loc[cRow][7])[11:16],df.loc[cRow][8],df.loc[cRow][9]), font=(fontSet, 40))
            showAnswer.grid(column=0, row=2)
            askLike = Label(app,text="Do you like it? : ")
            like_yes = Button(app, text="YES", command=app.destroy)
            like_no = Button(app, text="NO", command=likeIt)
            askLike.grid(column=0, row=3)
            like_yes.grid(column=1, row=3)
            like_no.grid(column=2, row=3)
            word = str(df.loc[cRow][1])
            url = requests.get('https://www.google.com/search?q={0}&tbm=isch'.format(word))

            soup = BeautifulSoup(url.text, 'lxml')
            images = soup.findAll('img')
            i = []
            raw_data = []
            im = []
            render = []
            for j in range(3) :
                i.append(random.choice(images))
                raw_data.append(urllib.request.urlopen(i[j].get('src')).read())
                im.append(Image.open(io.BytesIO(raw_data[j])))
                render.append(ImageTk.PhotoImage(im[j]))
            OutIMG1 = Label(app, image=render[0])
            OutIMG1.image = render[0]
            OutIMG1.grid(column=0, row=4)
            OutIMG2 = Label(app, image=render[1])
            OutIMG2.image = render[1]
            OutIMG2.grid(column=1, row=2)
            OutIMG3 = Label(app, image=render[2])
            OutIMG3.image = render[2]
            OutIMG3.grid(column=2, row=2)
        else :
            showUserAsk(1)
    else :
        showUserAsk(1)
def likeIt() :
    global askTryAgain, tryAgain_yes, tryAgain_no
    cRowShow.grid_forget()
    showAnswer.grid_forget()
    OutIMG1.grid_forget()
    OutIMG2.grid_forget()
    OutIMG3.grid_forget()
    askLike.grid_forget()
    like_yes.grid_forget()
    like_no.grid_forget()
    askTryAgain = Label(app,text="Do you want to try again? : ")
    tryAgain_yes = Button(app, text="YES", command=tryAgain)
    tryAgain_no = Button(app, text="NO", command=app.destroy)
    askTryAgain.grid(column=0, row=1)
    tryAgain_yes.grid(column=1, row=1)
    tryAgain_no.grid(column=2, row=1)

def tryAgain() :
    askTryAgain.grid_forget()
    tryAgain_yes.grid_forget()
    tryAgain_no.grid_forget()
    showUserAsk(1)
uso_submit = Button(app, text="SUBMIT", command=usoClicked)
def hideUserAsk() :
    uso_txt.grid_forget()
    uso_select1.grid_forget()
    uso_select2.grid_forget()
    uso_select3.grid_forget()
    uso_select4.grid_forget()
    uso_select5.grid_forget()
    uso_submit.grid_forget()
    uso_state_txt.grid_forget()
    
def showUserAsk(state) :
    uso_txt.grid(column=0, row=1)
    uso_select1.grid(column=0, row=1)
    uso_select2.grid(column=0, row=2)
    uso_select3.grid(column=0, row=3)
    uso_select4.grid(column=0, row=4)
    uso_select5.grid(column=0, row=5)
    uso_submit.grid(column=0, row=6)
    if state == 0 :
        uso_state_txt.configure(text="NEW!")
        uso_state_txt.grid(column=0, row=7)  
    elif state == 1 :
        uso_state_txt.configure(text="TRY AGAIN!")
        uso_state_txt.grid(column=0, row=7)


lbl.grid(column=0, row=0)
start_btn.grid(column=0, row=1)
app.mainloop()