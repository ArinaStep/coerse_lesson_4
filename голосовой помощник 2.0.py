import pyaudio
import random
import speech_recognition as sr

privetstviya=['Вот так встреча!',
'Всегда рады Вам',
'Глубокое (глубочайшее) почтение',
'Горячий привет!',
'Горячо приветствую',
'Доброго здоровья!',
'Доброе утро!',
'Добро пожаловать!',
'Добрый вечер!',
'Добрый день!',
'Дозвольте приветствовать (Вас)',
'Душевно рад (Вас видеть)',
'Душою рад Вас видеть',
'Желаю здравствовать!',
'Здравия желаю',
'Здравствуйте!',
'Какая встреча!' ]
films=['Чебурашка',"Аватар.путь воды","Мира","Движение вверх","Анчаред.На картах не значится","Человек-паук","Одна","Доктор Стрэндж: в мультивселенной безумия" ]
r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Скажите что-нибудь...')
        audio=r.listen(source)

    speech=r.recognize_google(audio,language='ru_RU').lower()
    print("Вы сказали :" ,speech )
    if speech == "привет":
        print((random.choice(privetstviya)).lower())
    if speech=="фильм":
        print("Могу посоветовать Вам фильм: ",(random.choice(films)).lower())
    if speech=='выйти':
        break
    else:
        print("неизвестная команда")