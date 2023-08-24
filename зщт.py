import telebot  # pyTelegramBotAPI
import requests
from bs4 import BeautifulSoup
import random
import time
from telebot import types

token = '6179435379:AAH1Zp0fvE2D1LfGEM579wzchEkJY3OV2Ug'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = "Привет! Я умею рассказывать стихи, интересные факты, показывать котиков"
    bot.send_message(message.chat.id, welcome)
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


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и всё стихотворение"
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button = telebot.types.InlineKeyboardButton("перейти", url='https://stihi.ru/')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    responce = requests.get('https://i-fakt.ru')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact.a.attrs['href'])


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = random.randint(1, 3)
    cat_img = open('cat' + str(cat_number) + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


@bot.message_handler(command=['audio'])
def send_song(message):
    responce = requests.get('https://europaplus.ru/programs')
    responce = responce.content
    html = BeautifulSoup(responce, 'lxml')
    songs = random.choice(html.find_all(class_='account'))
    bot.send_message(message.chat.id, songs.text)
    bot.send_message(message.chat.id, songs.a.attrs['href'])
    print(input('Какую программу вы хотите послушать? у нас на выбор есть: "бригада У" и т.д.'))
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(text='Бригада У', url='https://europaplus.ru/brigadau')
    markup.add(item)
    item1 = types.InlineKeyboardButton(text='Радиоактивное Шоу', url='https://europaplus.ru/rash')
    markup.add(item1)
    item2 = types.InlineKeyboardButton(text='Week&Star', url='https://europaplus.ru/week-and-star')
    markup.add(item2)
    item3 = types.InlineKeyboardButton(text='Крутой Уикенд', url='https://europaplus.ru/programs/krutoy-uikend')
    markup.add(item3)
    item4 = types.InlineKeyboardButton(text='Крутой Уикенд', url='https://europaplus.ru/programs/krutoy-uikend')
    markup.add(item4)
    # Лизка доделай там сама иначе ты нифига уже не делаешь!!!!!!


@bot.message_handler(command=['sticker'], func=lambda call: True)
def send_sticker(call):
    if call.data == '1':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(text='IT-куб', url='https://t.me/addstikers/it_cube_nn')
        markup.add(item)
        bot.send_message(call.message.chat.id, 'держи стикеры', reply_markup=markup)
        time.sleep(5)
        bot.answer_callback_query(call.id, show_alert=True, text='стикеры получены!')
        markup = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton(text='назад', callback_data='4')
        markup.add(item)
        time.sleep(2)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Котики':
        send_cat(message)
    elif message.text.strip() == 'Музыка':
        send_song(message)
    elif message.text.strip() == 'Стикер':
        send_sticker(message)
    elif message.text.strip() == 'Погода':
        send_pogoda(message)


@bot.message_handler(command=['play'])
def send_play(message):
    def g():
        print('сейчас я тебе покажу крутую игру в которую можно поиграть с удовльствием!')
        response = requests.get("https://store.steampowered.com/?l=russian")
        response = response.content

        html = BeautifulSoup(response, 'lxml')
        fact = random.choice(html.find_all(class_='p-2 clearfix'))
        print(fact.text)
        print(fact.a.attrs['href'])
        bot.send_play(message.chat.id)


@bot.message_handler(command=['interaktive game'])
class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

        def hit(self, target):
            if type(self) == type(target):
                target.health -= 20
            else:
                raise TypeError

        warriors = [Warrior('Воин1'), Warrior('Воин2')]
        while True:
            q = input(
                'Введите атака, чтобы воин1 атаковал.Введите атака2, чтобы воин2 атаковал. Для закрытия программы введите выключение: ')
            if q == 'атака':
                i = random.randint(0, 1)
                attacker, victim = warriors[i], warriors[i - 1]
                attacker.hit(victim)
                print(attacker.name, 'атаковал', victim.name)
                print('У', victim.name, 'осталось здоровья', victim.health)
                if victim.health <= 0:
                    print(attacker.name, 'поздравляю!вы победили!')
                    break
            if q == 'атака2':
                i = random.randint(0, 1)
                victim, attacker = warriors[i - 1], warriors[i]
                attacker.hit(victim)
                print(attacker.name, 'атаковал', victim.name)
                print('У', victim.name, 'осталось здоровья', victim.health)
                if victim.health <= 0:
                    print(attacker.name, 'поздравляю!вы победили!')
                    break
            elif q == 'выключение':
                break
            else:
                print('неизвестное значение')


@bot.message_handler(command=['pogoda'])
def send_pogoda(message):
    r = requests.get('https://sinoptik.ua/погода-нижний-новгород')
    code = BeautifulSoup(r.content, 'html.parser')
    for i in code.select('#contrnt'):
        min = i.select('.temperature.min')[0].text
        max = i.select('.temperature.max')[0].text
        text = i.select('.wDescription.description.')[0].text

        bot.send_pogoda(message.chat.id,
                        f'Погода на сегодняшний день: \n минимальная {min}, \n максимальная{max}, \n{text}')


bot.polling()
