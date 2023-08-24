from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry("400x400+230+200")
window.title("Панель валют")

img = PhotoImage(file='logo.png')
logo = Label(window, image = img)
logo.place(x=0, y=0)
lab = Label(window, text = "Курс валют \nот банка \nКод Будущего", font = "Arial 20")
lab.place(x=180, y=20)

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req" : today}
responce = requests.get(url, params = payload)
xml = BeautifulSoup(responce.content, features="xml")  #html.parser

def getCourse(id):
    return xml.find("Valute", {'ID': id}).Value.text

usd_course = Label(window, text = "$" + getCourse("R01235"), font = "Arial 16")
usd_course.place(x=150, y = 200)
eur_course = Label(window, text = "€"+getCourse('R01239'), font = "Arial 16")
eur_course.place(x = 150, y = 240)

course_date = Label(window, text = today.replace('/', '.'), font = "Arial 14")
course_date.place(x=145, y=300)


window.mainloop()