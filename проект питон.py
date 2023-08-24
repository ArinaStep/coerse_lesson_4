import telebot  # pyTelegramBotAPI
import requests
from bs4 import BeautifulSoup
import random
import time
from telebot import types
token = '6179435379:AAH1Zp0fvE2D1LfGEM579wzchEkJY3OV2Ug'
bot = telebot.TeleBot(token)
#Погода
r=requests.get('https://sinoptik.ua/погода-нижний-новгород')
code=BeautifulSoup(r.content, 'html.parser')
for i in code.select('#content'):
    min = i.select('.temperature .min')[0].text
    max = i.select('.temperature .max')[0].text
    text = i.select('.wDescription .description')[0].text
#Музыка
responce = requests.get('https://europaplus.ru/programs')
responce = responce.content
html = BeautifulSoup(responce, 'html.parser')
songs = html.find_all(class_='typography typography_mark_medium typography_type_subtitle typography_size_max card__body__title')
spisok=[c.text for c in songs]
songs1 = html.find_all(class_='typography typography_mark_light typography_type_text typography_size_middle')
spisok1=[c1.text for c1 in songs1]
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = "Привет! Я умею рассказывать стихи, интересные факты, показывать котиков"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Стихотворение')
    button3 = telebot.types.KeyboardButton('Музыка')
    button4 = telebot.types.KeyboardButton('Стикер')
    button5 = telebot.types.KeyboardButton('Котики')
    button6 = telebot.types.KeyboardButton('Погода')
    button7 = telebot.types.KeyboardButton('Совет по игре')
    button8 = telebot.types.KeyboardButton('Интерактивная игра')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)
    bot.send_message(message.chat.id, welcome, reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def send_poem(message):
    if message.text=='Стихотворение':
        poem_text = "Муха села на варенье, вот и всё стихотворение"
        bot.send_message(message.chat.id, poem_text)
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        button = telebot.types.InlineKeyboardButton("перейти", url='https://stihi.ru/')
        keyboard.add(button)
        bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keyboard)
    if message.text=='Факт':
        responce = requests.get('https://i-fakt.ru')
        responce = responce.content
        html = BeautifulSoup(responce, 'html.parser')
        fact = random.choice(html.find_all(class_='p-2 clearfix'))
        bot.send_message(message.chat.id, fact.text)
        bot.send_message(message.chat.id, fact.a.attrs['href'])
    if message.text == 'Котики':
        cat_number = random.randint(1, 3)
        if cat_number==2:
            cat_img = open('cat' + str(cat_number) + '.jpg', 'rb')
            bot.send_photo(message.chat.id, cat_img)
        else:
            cat_img = open('cat' + str(cat_number) + '.jpeg', 'rb')
            bot.send_photo(message.chat.id, cat_img)
    if message.text == 'Музыка':
        for i in range(0, len(spisok)-1):
            bot.send_message(message.chat.id, f'👉{spisok[i]}. {spisok1[i]}👈')
        time.sleep(3)
        markup = types.InlineKeyboardMarkup(row_width=2)
        item = types.InlineKeyboardButton(text='Бригада У', url='https://europaplus.ru/brigadau')
        item1 = types.InlineKeyboardButton(text='Радиоактивное Шоу', url='https://europaplus.ru/rash')
        item2 = types.InlineKeyboardButton(text='Week&Star', url='https://europaplus.ru/week-and-star')
        item3 = types.InlineKeyboardButton(text='Крутой Уикенд', url='https://europaplus.ru/programs/krutoy-uikend')
        item4 = types.InlineKeyboardButton(text='Крутой Уикенд', url='https://europaplus.ru/programs/krutoy-uikend')
        markup.add(item, item1, item2, item3, item4)
        bot.send_message(message.chat.id,
                         'Какую программу вы хотите послушать? у нас на выбор есть: "бригада У" и т.д.', reply_markup=markup)
    if message.text == 'Стикер':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton(text='IT-куб', url='https://t.me/addstickers/Neymark2022')
        markup.add(item)
        bot.send_message(message.chat.id, 'держи стикеры', reply_markup=markup)
    if message.text == 'Погода':
        bot.send_message(message.chat.id, f'Погода на сегодняшний день: \n\n{min}, {max}\n\n🌤{text}')
    if message.text == 'Совет по игре':
        bot.send_message(message.chat.id, 'Сейчас я тебе покажу крутую игру в которую можно поиграть с удовльствием!')
        response = requests.get("https://store.steampowered.com/?l=russian")
        response = response.content
        html = BeautifulSoup(response, 'html.parser')
        fact = random.choice(html.find_all(class_='tab_item_name')) #p-2 clearfix
        bot.send_message(message.chat.id, fact.text)
    if message.text=='Интерактивная игра':
        bot.send_message(message.chat.id, 'Введите атака, чтобы воин атаковал вашего воина.')
    if  message.text=='атака':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        button1 = telebot.types.KeyboardButton('Воин 🏋')
        button2 = telebot.types.KeyboardButton('Воин 🧘')
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, 'Выберите за какого воина вы будете играть', reply_markup=keyboard)
    if message.text == 'Воин 🏋':
        # health здоровье вашего персонажа
        # health1 здоровье противника
        health = 100
        health1 = 100
        warriors = ['Воин 🏋', 'Воин 🧘']
        while health > 0:
            i = random.randint(0, 1)
            attacker, victim = warriors[i], warriors[i - 1]
            if attacker == 'Воин 🏋':
                health1 -= 20
                health += 5
                bot.send_message(message.chat.id,
                                 f'Атаковал {warriors[i]}, осталось здоровья соперника {health1}, осталось здоровья вашего персонажа {health}')
                time.sleep(2)
            if attacker == 'Воин 🧘':
                health -= 20
                health1 += 5
                bot.send_message(message.chat.id,
                                 f'Атаковал {warriors[i]}, осталось здоровья соперника {health1}, осталось здоровья вашего персонажа {health}')
                time.sleep(2)
            if health1 <= 0:
                bot.send_message(message.chat.id, 'Поздравляю! Вы победили!')
                break
            if health <= 0:
                bot.send_message(message.chat.id, 'Увы! Вы проиграли!')
                break
    if message.text == 'Воин 🧘':
        health = 100
        health1 = 100
        warriors = ['Воин 🏋', 'Воин 🧘']
        while health > 0:
            i = random.randint(0, 1)
            attacker, victim = warriors[i], warriors[i - 1]
            if attacker=='Воин 🏋':
                health1+=5
                health-=20
                bot.send_message(message.chat.id, f'Атаковал {warriors[i]}, осталось здоровья соперника {health1}, осталось здоровья вашего персонажа {health}')
                time.sleep(2)
            if attacker=='Воин 🧘':
                health+=5
                health1-=20
                bot.send_message(message.chat.id, f'Атаковал {warriors[i]}, осталось здоровья соперника {health1}, осталось здоровья вашего персонажа {health}')
                time.sleep(2)
            if health1 <= 0:
                bot.send_message(message.chat.id, 'Поздравляю! Вы победили!')
                break
            if health <= 0:
                bot.send_message(message.chat.id, 'Увы! Вы проиграли!')
                break
bot.polling()