import telebot
import requests
from bs4 import BeautifulSoup
import random

token='5699721407:AAHItXdddfsQ5N2zsQJrGjeZQFGjRgkAzwk'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome='привет! я умею рассказывать стихи, интересные факты, показывать котиков'
    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text='Муха села на варенье, вот и всё стихотворение'
    bot.send_message(message.chat.id,poem_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    responce = requests.get('https://i-fakt.ru')
    responce = responce.content
    html=BeautifulSoup(responce,'lxml')
    fact=random.choice(html.find_all(class_='p-2 clearfix'))

    bot.send_message(message.chat.id,fact.text)
    bot.send_message(message.chat.id,fact.a.attrs['href'])

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_img=open('img_cat.jpg','rb')
    bot.send_photo(message.chat.id, cat_img)

bot.polling()