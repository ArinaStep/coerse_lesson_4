# wool_style_bot
#привествую имя! меня зовут екатерина, я вяжу ежедневно уже более 7 лет и делюсь знаниями в своём блоге.Переходите по ссылке и пользуйтесь гайдом.
#не забудьте подписаться на мой тг канал:
#галка зеленая, нажмите на кнопку подписаться и я вас буду ждать на канале где есть много полезной и важной информации
#другая галка, после подписки возвращайтесь в чат-бот, нажимайте на подписалась и я пришлю вам подарок
#если человек подписан на канал(ССЫЛКА) то отлично нажимайте на файлик и получите подарок.
import telebot  # pyTelegramBotAPI
from telebot import types
import time
from telebot.apihelper import ApiTelegramException
token = '6179435379:AAH1Zp0fvE2D1LfGEM579wzchEkJY3OV2Ug'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_poem(message):
    if message.text=='help' or 'start':
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        button = telebot.types.InlineKeyboardButton("Подписаться", url='https://t.me/polezno_woolstyle')
        keyboard.add(button)
        button1 = telebot.types.InlineKeyboardButton("Подписалась(лся)", url='https://drive.google.com/file/d/1e10QvLtje9YRDo-oej4UF8w-BTNQ-jsV/view?usp=drivesdk')
        keyboard.add(button1)
        #     markup = types.InlineKeyboardMarkup()
        #     bot.send_message(bot.message.chat.id, 'держи стикеры', reply_markup=markup)
        #     time.sleep(5)
        #     bot.answer_callback_query(bot.id, show_alert=True, text='стикеры получены!')
        #     markup = types.InlineKeyboardMarkup(row_width=1)
        #     item = types.InlineKeyboardButton(text='назад', callback_data='4')
        #     markup.add(item)
        #     time.sleep(2)
        bot.send_message(message.chat.id, 'Привествую!Меня зовут Екатерина, я вяжу ежедневно уже более 7 лет и делюсь знаниями в своём блоге.Переходите по ссылке и пользуйтесь гайдом.\n \n ✅Нажмите на кнопку "Подписаться", и я Вас буду ждать в своём канале, где Вы найдёте много полезной информации\n✅После подписки возвращайтесь в чат-бот, нажимайте на "Подписалась(лся)", и я пришлю Вам подарок.', reply_markup=keyboard)

bot.polling()


#
# def is_subscribed(chat_id, user_id):
#     try:
#         bot.get_chat_member(chat_id, user_id)
#         return True
#     except ApiTelegramException as e:
#         if e.result_json['description'] == 'Bad Request: user not found':
#             return False
#
# if not is_subscribed(CHAT_ID, USER_ID):
#     # user is not subscribed. send message to the user
#     bot.send_message(CHAT_ID, 'Please subscribe to the channel')
# else:
#      user is subscribed. continue with the rest of the logic

# @bot.message_handler(command=['sticker'],func=lambda call:True)
# def send_sticker(call):
#     if call.data == '1':
#         markup = types.InlineKeyboardMarkup()
#         item = types.InlineKeyboardButton(text='IT-куб', url='https://t.me/addstikers/it_cube_nn')
#         markup.add(item)
#         bot.send_message(call.message.chat.id, 'держи стикеры', reply_markup=markup)
#         time.sleep(5)
#         bot.answer_callback_query(call.id, show_alert=True, text='стикеры получены!')
#         markup = types.InlineKeyboardMarkup(row_width=1)
#         item = types.InlineKeyboardButton(text='назад', callback_data='4')
#         markup.add(item)
#         time.sleep(2)
lst=[1,2,3,4,5]
num=int(input())
print(lst[num% len(lst)-1])
