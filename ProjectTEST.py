from tkinter import *
import requests
from bs4 import BeautifulSoup
import random
import io
import urllib
from PIL import Image, ImageTk
app = Tk()
app.title("Do you want something to eat?")
app.geometry('1280x720')

word = 'dog'
url = requests.get('https://www.google.com/search?q={0}&tbm=isch'.format(word))

soup = BeautifulSoup(url.text, 'lxml')
images = soup.findAll('img')

i = random.choice(images)
print(i.get('src'))
raw_data = urllib.request.urlopen(i.get('src')).read()
im = Image.open(io.BytesIO(raw_data))
image = ImageTk.PhotoImage(im)
label1 = Label(app, image=image)
label1.grid(row=0)
app.mainloop()